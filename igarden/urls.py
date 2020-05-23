from django.urls import path, include
from . import views


urlpatterns = [
    path('lists/', include('lists.urls')),
    path('', views.home, name='igarden-home'),
    path('search/', views.search, name='igarden-search'),
    path('explore/', views.Explore.as_view(), name='igarden-explore')
]
