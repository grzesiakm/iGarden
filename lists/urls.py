from django.urls import path
from . import views


urlpatterns = [
    path('lists/', views.Lists.as_view(), name='lists-lists'),
    path('fav/', views.fav, name='lists-fav'),
    path('create_list/', views.create_list, name='lists-create-list')
]
