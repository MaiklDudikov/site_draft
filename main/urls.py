from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_register, name='main_register'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('list_users', views.list_users, name='list_users'),
    path('register/', views.register, name='register'),
    path('video/', views.video, name='video'),
]
