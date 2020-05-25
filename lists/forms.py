from django import forms
from igarden.models import Flower
from lists.models import UserFlowersList


class CreateListForm(forms.Form):
    class Meta:
        model = UserFlowersList

    name = forms.CharField(max_length=100)
    elements = forms.ModelMultipleChoiceField(queryset=Flower.objects.all())


class AddToListForm(forms.Form):
    class Meta:
        model = UserFlowersList

    elements = forms.ModelMultipleChoiceField(queryset=UserFlowersList.objects.all())