from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.contrib.auth import login, get_user_model
from task_app.models import Task
from task_app.forms import TaskForm


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_app/task_detail.html"
    context_object_name = "task"

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return super().get(request, *args, **kwargs)


class TaskListView(ListView):
    model = Task
    template_name = "task_app/task_list.html"
    context_object_name = "task_list"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        user_company = self.request.user.company
        if user_company:
            queryset = queryset.filter(company=user_company)

        return queryset.order_by("-created_at")


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_app/task_add.html"
    form_class = TaskForm
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_app/task_update.html"
    form_class = TaskForm
    success_url = reverse_lazy("task_list")


def index(request):
    return render(request, "task_app/index.html")


def close_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.status = "COMPLETED"
        task.save()
        messages.success(request, f"Задача '{task.title}' успешно завершена")
    return redirect("task_list")


@login_required(login_url="/login/")
def team(request):
    team = request.user.company.employees.all() if request.user.company else []
    context = {
        "company_id": request.user.company.id if request.user.company else None,
        "team": team,
    }
    return render(request, "task_app/team.html", context=context)
