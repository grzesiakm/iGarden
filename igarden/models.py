from django.db import models

class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)
    treatment = models.TextField()

    def __str__(self):
        return self.name
