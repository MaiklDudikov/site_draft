from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def list_users(request):
    users_psw = User.objects.all()
    return render(request, 'main/list_users.html', {'user' : users_psw})


def profile(request):
    name = request.POST.get("name", "Undefined")
    return render(request, 'main/profile.html', {'user' : name})


def login(request):
    return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')


def video(request):
    return render(request, 'main/video.html')


def main_register(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('profile')

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/register.html', data)
