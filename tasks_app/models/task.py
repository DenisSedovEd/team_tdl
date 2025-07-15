from django.db import models

from tasks_app.models.task_status import TaskStatus


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        TaskStatus,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
