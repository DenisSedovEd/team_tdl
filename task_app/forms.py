from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from task_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "deadline", "user", "parent_task"]
        labels = {
            "title": "Название",
            "description": "Описание",
            "deadline": "Крайний срок",
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
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "placeholder": "Крайний срок",
                },
                format="%Y-%m-%d",
            ),
            "user": forms.Select(attrs={"class": "form-select"}),
            "parent_task": forms.Select(attrs={"class": "form-select"}),
            "company": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        queryset_tasks = Task.objects.exclude(status="COMPLETED").order_by(
            "-created_at"
        )
        User = get_user_model()
        if user:
            self.fields["user"].initial = user
            if user.company:
                queryset_tasks = queryset_tasks.filter(company=user.company)
                self.fields["user"].queryset = user.company.employees.all()
            else:
                queryset_tasks = queryset_tasks.filter(user=user)
                self.fields["user"].queryset = User.objects.filter(pk=user.pk)
        self.fields["parent_task"].queryset = queryset_tasks

        if self.instance and self.instance.pk:
            self.fields["parent_task"].queryset = self.fields[
                "parent_task"
            ].queryset.exclude(id=self.instance.pk)
