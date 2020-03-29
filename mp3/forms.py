from django import forms

class UploadFileForm(forms.Form):
    mp3_file = forms.FileField()