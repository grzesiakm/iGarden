from django import forms

class UploadPhotoForm(forms.Form):
    file = forms.FileField(label='')
