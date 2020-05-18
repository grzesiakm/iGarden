from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='igarden-home'),
    path('lists/', views.Lists.as_view(), name='igarden-lists'),
    path('search/', views.search, name='igarden-search'),
    path('explore/', views.Explore.as_view(), name='igarden-explore'),
    path('fav/', views.fav, name='igarden-fav'),
    path('create_list/', views.create_list, name='igarden-create-list')
]
