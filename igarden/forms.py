from django import forms
from .models import Flower

class UploadPhotoForm(forms.Form):
    file = forms.FileField(label='')

class Choose_flower(forms.Form):
    class Meta:
        model = Flower

    element = forms.ModelChoiceField(queryset=Flower.objects.all())