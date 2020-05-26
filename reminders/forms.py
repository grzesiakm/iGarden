from django import forms
from .models import Reminder


class ReminderForm(forms.Form):

    class Meta:
        model = Reminder

frequency_in_days = forms.IntegerField()