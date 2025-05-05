from django.forms import forms, CharField, FileField, Textarea


class GenerateContentForm(forms.Form):
    requirement_text = CharField(
        widget=Textarea(attrs={'rows': 5, 'cols': 40}),
        label="Provide your requirements here.",
        required=False
    )
    requirement_doc = FileField(label="Provide your requirements file here.", required=False)
