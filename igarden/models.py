from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import Profile

class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    flower_photo = models.ImageField(upload_to='images/', blank=True)
    treatment = models.TextField()

    def __str__(self):
        return self.name

class UserFlowersList(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    elements = models.ManyToManyField(Flower)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flower-detail', kwargs={'pk': self.pk})
