from django.forms import forms, CharField, FileField


class GenerateContentForm(forms.Form):
    requirement_text = CharField(max_length=100)
    requirement_doc = FileField()
