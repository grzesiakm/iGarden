from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='igarden-home'),
    path('lists/', views.lists, name='igarden-my-lists'),
]
