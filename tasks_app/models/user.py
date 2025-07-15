from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    position = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
