from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from django.shortcuts import render

from .forms import GenerateContentForm
from django.views import View


# Create your views here.

class GenerateScopeView(View):
    def get(self, request):
        context = {}
        context['form'] = GenerateContentForm()
        return render(request, "agents/generate_scope.html", context)

    def post(self, request):
        context = {}
        breakpoint()
        context['form'] = GenerateContentForm()
        file_path = '/home/kevit/PycharmProjects/scope_django/scope_agency/agents/templates/file.txt'
        # try:
        #     with open(file_path, 'w') as file:
        #         file.write("abc")
        #         response = HttpResponse(file_data, content_type='text/plain')
        #         response['Content-Disposition'] = 'attachment; filename="file.txt"'
        #         return response

        # except FileNotFoundError:
        #     return HttpResponseNotFound("File not found")
        # return render(request, "agents/generate_scope.html", context)
        return FileResponse(