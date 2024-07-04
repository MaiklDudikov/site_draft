from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=234)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человека'
        verbose_name_plural = 'Люди'
