import os, io, uuid
from pathlib import Path
from functools import wraps

import PyPDF2
import docx
from msal import ConfidentialClientApplication
from django.http import FileResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render

from .scope_agency_individual_agents.main_redefined import generate_graph
from .forms import GenerateContentForm
from .utils import get_logger

logger = get_logger("views")


def ms_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.session.get('is_authenticated'):
            return redirect('ms_login')
        return view_func(request, *args, **kwargs)

    return _wrapped


def ms_login(request):
    # Create MSAL app
    msal_app = ConfidentialClientApplication(
        client_id=settings.MSAL_CLIENT_ID,
        client_credential=settings.MSAL_CLIENT_SECRET,
        authority=settings.MSAL_AUTHORITY,
    )
    # Build auth URL
    state = str(uuid.uuid4())
    request.session['auth_state'] = state
    auth_url = msal_app.get_authorization_request_url(
        scopes=settings.MSAL_SCOPE,
        state=state,
        redirect_uri=request.build_absolute_uri('/msal/callback/')
    )
    return redirect(auth_url)


def ms_callback(request):
    # Validate state
    if request.GET.get('state') != request.session.get('auth_state'):
        return redirect('ms_login')
    msal_app = ConfidentialClientApplication(
        client_id=settings.MSAL_CLIENT_ID,
        client_credential=settings.MSAL_CLIENT_SECRET,
        authority=settings.MSAL_AUTHORITY,
    )
    # Exchange code for token
    result = msal_app.acquire_token_by_authorization_code(
        code=request.GET.get('code'),
        scopes=settings.MSAL_SCOPE,
        redirect_uri=request.build_absolute_uri('/msal/callback/')
    )
    if 'id_token' in result:
        # Mark session as authenticated
        request.session['is_authenticated'] = True
        request.session['user_name'] = result.get('id_token_claims', {}).get('name')
        return redirect('generate-scope')
    return render(request, 'error.html', {'error': result.get('error_description')})


@method_decorator(ms_required, name='dispatch')
class GenerateScopeView(View):
    template_name = "agents/generate_scope.html"

    def get(self, request):
        return render(request, self.template_name, {'form': GenerateContentForm()})

    def post(self, request):
        try:
            form = GenerateContentForm(request.POST, request.FILES)
            if not form.is_valid():
                return HttpResponseBadRequest("Invalid form submission")

            text = form.cleaned_data['requirement_text']
            uploaded_file = form.cleaned_data['requirement_doc']
            uploaded_content = None
            if not text and not uploaded_file:
                message = "Please provide either text or document!"
                messages.error(request, message)
                logger.error(f"Error: {message}")
                return render(request, self.template_name, {'form': form})
            if text and uploaded_file:
                message = "Please provide either text or document, not both!"
                messages.error(request, message)
                logger.error(f"Error: {message}")
                return render(request, self.template_name, {'form': form})
            if uploaded_file:
                logger.info("Received input as file. Converting to text.")
                filename = uploaded_file.name
                ext = os.path.splitext(filename)[1].lower()
                file_obj = uploaded_file.file
                if ext == '.txt':
                    uploaded_content = file_obj.read().decode('utf-8')
                elif ext == '.pdf':
                    reader = PyPDF2.PdfReader(file_obj)
                    uploaded_content = ''.join([page.extract_text() or '' for page in reader.pages])
                elif ext == '.docx':
                    uploaded_content = '\n'.join([para.text for para in docx.Document(file_obj).paragraphs])
                else:
                    logger.error(f"Unsupported file: {uploaded_file.filename}")

            if text:
                logger.info("Received input as text.")
            data = text or uploaded_content
            output = generate_graph(data)
            if output:
                message = "Document created successfully."
                logger.info(message)
                messages.success(request, message)
                file = open(f"{Path(__file__).resolve().parent.parent}/scope_pipeline/all_content.md", 'rb')
                return FileResponse(
                    file,
                    as_attachment=True,
                    filename="your_text.md",
                    content_type='text/markdown'
                )
            else:
                message = "Error creating document."
                logger.error(message)
                messages.error(request, message)
                return render(request, self.template_name, {'form': GenerateContentForm()})
        except Exception as error:
            message = f"Exception occurred : {error}"
            logger.error(message)
            messages.error(request, message)
            return render(request, self.template_name, {'form': GenerateContentForm()})
