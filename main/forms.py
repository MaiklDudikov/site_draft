from .models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите никнейм',
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль',
            })
        }
