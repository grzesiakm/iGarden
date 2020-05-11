from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='igarden-home'),
    path('lists/', views.lists, name='igarden-lists'),
    path('search/', views.search, name='igarden-search')
]
