from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Reminder, Flower
from .forms import ReminderForm

@login_required
def send(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            new_remider = Reminder()
            new_reminder.message = 'Do not forget to water your plant today!'
            new_remider.recipient = request.user
            new_reminder.about = Flower.objects.filter(name='')[0]
            new_remider.frequency_in_days = form.cleaned_data[1]
            new_reminder.save()
            send_mail(
                'Water Reminder from your iGarden!',
                new_remider.message,
                'marta1317.mg@gmail.com',
                [new_remider.recipient],
                fail_silently=False,
            )
        return render(request, 'list/list_detail.html')
    else:
        form = ReminderForm()
        return render(request, 'lists/list_detail.html', {'form': form})