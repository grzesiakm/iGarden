from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from igarden.models import Flower

class Reminder(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.OneToOneField(Flower, on_delete=models.CASCADE)
    frequency_in_days = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.about