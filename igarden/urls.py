from django.urls import path
from .views import FlowerListView, FlowerDetailView, ListCreateView, ListUpdateView, ListDeleteView
from . import views


urlpatterns = [
    path('', views.home, name='igarden-home'),
    path('lists/', FlowerListView.as_view(), name='igarden-lists'),
    path('list/<int:pk>/', FlowerDetailView.as_view(), name='flower-detail'),
    path('list/new/', ListCreateView.as_view(), name='flower-create'),
    path('list/<int:pk>/update/', ListUpdateView.as_view(), name='flower-update'),
    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name='flower-delete'),
    path('search/', views.search, name='igarden-search'),
]
