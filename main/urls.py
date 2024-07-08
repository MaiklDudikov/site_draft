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

# 1. Удалите существующую базу данных (если это возможно):
# rm db.sqlite3

# 2. Удалите существующие файлы миграций (кроме __init__.py):
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete

# 3. Создайте новые миграции для всех приложений:
# python manage.py makemigrations
# python manage.py migrate

# 4. Проверка создания суперпользователя :
# python manage.py createsuperuser
