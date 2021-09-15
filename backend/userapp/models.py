from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)

