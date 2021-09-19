from django.contrib.auth.models import AbstractUser
from django.db import models


class ToDoUser(AbstractUser):
    """модель пользователя ToDoUser, наследованная от абстрактного"""
    email = models.EmailField(
        verbose_name='email',
        max_length=64,
        unique=True)
