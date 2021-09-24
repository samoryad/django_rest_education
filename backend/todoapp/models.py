from django.db import models
from userapp.models import ToDoUser


class Project(models.Model):
    """модель проекта"""
    name = models.CharField(
        max_length=128,
        verbose_name='название проекта',
        unique=True)
    link = models.CharField(
        max_length=128,
        verbose_name='ссылка на репозиторий')
    users = models.ManyToManyField(ToDoUser, verbose_name='пользователи')


class ToDo(models.Model):
    """модель заметок"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name='проект заметки')
    text = models.TextField(verbose_name='текст заметки')
    created_date = models.DateTimeField(
        verbose_name='дата создания', auto_now_add=True)
    updated_date = models.DateTimeField(
        verbose_name='дата обновления', auto_now=True)
    user = models.ForeignKey(
        ToDoUser,
        on_delete=models.CASCADE,
        verbose_name='пользователь')
    is_active = models.BooleanField(default=True, verbose_name='активна')
