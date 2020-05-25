from django.urls import path
from . import views


urlpatterns = [
    path('', views.Lists.as_view(), name='lists-all'),
    path('lists/', views.Lists.as_view(), name='lists-all'),
    path('fav/', views.fav, name='lists-fav'),
    path('create_list/', views.create_list, name='lists-create-list'),
    path('<int:id>/see_list/', views.ListDetailView.as_view(), name='lists-see-list'),
    path('<int:id>/delete_list/', views.ListDeleteView.as_view(), name='lists-delete-list'),
]
