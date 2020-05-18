from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    flower_photo = models.ImageField(upload_to='images/', blank=True)
    treatment = models.TextField()

    def __str__(self):
        return self.name


class UserFlowersList(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    elements = models.ManyToManyField(Flower)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
