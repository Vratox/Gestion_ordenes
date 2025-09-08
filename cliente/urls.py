from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cliente_view.as_view(), name='cliente'),
    path('ClienteJson/', views.ClienteJsonView.as_view(), name='clienteJson')
    
]