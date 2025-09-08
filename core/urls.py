from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login_views.as_view(), name='login_user'),
    path('logout/', views.Logout_view.as_view(), name='logout_user'),  
    path('home/', views.Home_view.as_view(), name='home'),
    path('repeatPassword/', views.RepeatPasswordView.as_view(), name='repeat_password')
]