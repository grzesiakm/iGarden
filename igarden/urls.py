from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='igarden-home'),
    path('lists/', views.lists, name='igarden-lists'),
    path('search/', views.search, name='igarden-search'),
    path('explore/', views.Explore.as_view(), name='igarden-explore'),
    path('fav/', views.fav, name='igarden-fav'),
]
