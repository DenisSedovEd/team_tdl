"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from task_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/", views.TaskListView.as_view(), name="task_list"),
    path("task/<int:pk>", views.TaskDetailView.as_view(), name="task_detail"),
    path("task/add/", views.TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:task_id>/completed", views.close_task, name="task_completed"),
    path("team/", views.team, name="team"),
]
