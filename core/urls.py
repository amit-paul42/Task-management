from django.contrib import admin
from django.urls import path
from core.views import index, task_create, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('create/', task_create, name='task_create'),
    path('delete/<int:pk>', delete_task, name='task_delete'),
]