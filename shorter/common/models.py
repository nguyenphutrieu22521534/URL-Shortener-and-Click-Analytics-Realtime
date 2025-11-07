from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_login = None
    is_staff = None
    is_superuser = None
    username = None

    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []