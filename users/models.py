from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from igarden.models import Flower

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_default.jpg', upload_to='profile_pics')
    favourites = models.ManyToManyField(Flower, related_name='favoured_by')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
