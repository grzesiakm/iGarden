from django.db import models


# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    treatment = models.TextField()

    def __str__(self):
        return Flower.name
