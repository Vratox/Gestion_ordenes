from django.contrib import admin
from django.urls import path
from ordenes import views


urlpatterns = [
    path('', views.ordenes_view.as_view(), name='ordenes'),
    path('tableJson/', views.tableOrdenesJsonView.as_view(), name='tableOrdenesJson'),
    
]