from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        help_texts = {
            'task_title': 'Enter the task name',
            'task_description': 'Enter the task description',
            'task_assign_date': 'Enter the task due date',
            'task_category': 'Select the task category',
        }
        error_messages = {
            'task_title': {
                'required': "Task name is required",
                'max_length': "Task name should be less than 100 characters"
            },
            'task_description': {
                'required': "Task description is required",
                'max_length': "Task description should be less than 500 characters"
            },
            'task_assign_date': {
                'required': "Task due date is required",
            },
            'task_category': {
                'required': "Task category is required",
            }
        }
        widgets ={
            'task_assign_date': forms.DateInput(attrs={'type': 'date'})
        }


