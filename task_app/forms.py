from django import forms
from django.core.exceptions import ValidationError

from task_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "user", "parent_task"]
        labels = {
            "title": "Название",
            "description": "Описание",
            "user": "Исполнитель",
            "parent_task": "Главная задача",
            "company": "Компания",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название",
                }
            ),
            "user": forms.Select(attrs={"class": "form-select"}),
            "parent_task": forms.Select(attrs={"class": "form-select"}),
            "company": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["parent_task"].queryset = Task.objects.exclude(
            status="COMPLETED"
        ).order_by("-created_at")

        if self.instance and self.instance.pk:
            self.fields["parent_task"].queryset = self.fields[
                "parent_task"
            ].queryset.exclude(id=self.instance.pk)
