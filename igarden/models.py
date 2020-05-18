from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    flower_photo = models.ImageField(upload_to='images/', blank=True)
    treatment = models.TextField()

    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=20)
    date_searched = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    flower_names = models.ManyToManyField(Flower)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flower-detail', kwargs={'pk': self.pk})
