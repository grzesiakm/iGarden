from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='igarden-home'),
    path('search/', views.search, name='igarden-search'),
    path('explore/', views.detail, name='igarden-explore'),
    path('<int:id>/list_add/', views.add_to_list, name='igarden-add'),
    path('<int:id>/list_add_to_fav/', views.add_to_fav, name='igarden-add-to-fav'),
]
