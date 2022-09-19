from django.urls import path
from . import views
  
urlpatterns = [
    path('login/', views.login, name='login'),
    path('clients/', views.clients, name='clients'),
    path('produits/', views.produits, name='produits'),
]