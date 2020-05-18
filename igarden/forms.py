from django import forms
from igarden.models import Flower, UserFlowersList

class UploadPhotoForm(forms.Form):
    file = forms.FileField(label='')


class CreateListForm(forms.Form):
    class Meta:
        model = UserFlowersList

    name = forms.CharField(max_length=100)
    elements = forms.ModelMultipleChoiceField(queryset=Flower.objects.all())
