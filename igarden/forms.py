from django import forms
from igarden.models import Flower

class UploadPhotoForm(forms.Form):
    file = forms.FileField(label='')


class CreateListForm(forms.Form):
    name = forms.CharField(max_length=100)
    elements = forms.ModelMultipleChoiceField(queryset=Flower.objects.all())
