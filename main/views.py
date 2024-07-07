from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


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


def list_users(request):
    users_psw = User.objects.all()
    return render(request, 'main/list_users.html', {'user' : users_psw})


# "Undefined"
# @login_required
# {'user': request.user}
def profile(request):
    name = request.POST.get("name", "Undefined")
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    return render(request, 'main/profile.html', {'user' : name})


def login(request):
    return render(request, 'main/login.html')


# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         password = request.POST.get('password')
#         # user = authenticate(request, name=name, password=password)
#         if user is not None:
#             # auth_login(request, user)
#             return redirect('profile')
#         else:
#             error = 'Такого пользователя не существует'
#             return render(request, 'main/login.html', {'error': error})

#     return render(request, 'main/login.html')


def register(request):
    return render(request, 'main/register.html')


def video(request):
    return render(request, 'main/video.html')
