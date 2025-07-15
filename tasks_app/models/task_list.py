from django.db import models

from tasks_app.models.user import User
from tasks_app.models.task import Task


class TaskList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    executor = models.ManyToManyField(
        User,
        related_name="tasks",
    )
    tasks = models.OneToOneField(
        Task,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
