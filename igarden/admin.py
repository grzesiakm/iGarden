from django.contrib import admin
from .models import Flower, UserFlowersList

# Register your models here.
admin.site.register(Flower)
admin.site.register(UserFlowersList)
