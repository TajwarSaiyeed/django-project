from django.urls import path

from .views import add_task, edit_task, delete_task

urlpatterns = [
    path('add-task/', add_task, name='add_task'),
    path('edit/<int:task_id>/', edit_task, name="edit_task"),
    path('delete/<int:task_id>/', delete_task, name="delete_task"),
]
