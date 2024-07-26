from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_space, name='space'),
    path('regist/', views.registration, name='regist'),
    path('plans/', views.plans, name='plans'),
    path('bets/', views.bets, name='bets'),
    path('investments/', views.investments, name='investments'),
    path('doors/', views.index, name='doors'),
    path('films/', views.my_films, name='films'),
    path('psw/', views.database_users, name='psw'),
]
