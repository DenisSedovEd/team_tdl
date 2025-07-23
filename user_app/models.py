from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Имя пользователя",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
    )
    position = models.CharField(
        max_length=150,
        blank=False,
        null=False,
    )
    subordinate_to = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="subordinates",
        null=True,
        blank=True,
        verbose_name="Руководитель",
    )
    under_his_command = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="under_his_commands",
        null=True,
        blank=True,
        verbose_name="Подчиненные",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
