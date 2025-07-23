from django.db import models
from typing import ClassVar, Tuple
from django.utils import timezone

from task_app.apps import TaskAppConfig
from user_app.models import CustomUser, Company


class TaskStatus(models.TextChoices):
    IN_PROGRESS: ClassVar[Tuple[str, str]] = "IN_PROGRESS", "В работе"
    COMPLETED: ClassVar[Tuple[str, str]] = "COMPLETED", "Завершена"
    PENDING: ClassVar[Tuple[str, str]] = "PENDING", "Ожидание"
    CANCELLED: ClassVar[Tuple[str, str]] = "CANCELLED", "Отменена"


class Task(models.Model):
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        unique=True,
        verbose_name="Заголовок задачи",
    )
    description = models.TextField(
        blank=False, null=False, unique=False, verbose_name="Описание задачи"
    )
    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        verbose_name="Статус задачи",
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        default=timezone.now,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Исполнитель",
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Главная задача",
        related_name="parent_tasks",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Компания",
    )
