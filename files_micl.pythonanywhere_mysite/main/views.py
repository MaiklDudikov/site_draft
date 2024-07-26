from django.shortcuts import render  # redirect
from .models import User


def main_space(request):
    return render(request, 'main/main_space.html')


def registration(request):
    return render(request, 'main/regist.html')


def plans(request):
    return render(request, 'main/plans.html')


def bets(request):
    return render(request, 'main/bets.html')


def investments(request):
    return render(request, 'main/invest.html')


def database_users(request):
    users_psw = User.objects.all()
    return render(request, 'main/database_users.html', {'user': users_psw})


def my_films(request):
    return render(request, 'main/my_films.html')


def about(request):
    return render(request, 'main/about.html')


def index(request):
    return render(request, 'main/index.html')
