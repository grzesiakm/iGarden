from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from igarden.models import Flower


class UserFlowersList(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    elements = models.ManyToManyField(Flower)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
