from django.shortcuts import render, redirect
from task.forms import TaskForm
from task.models import Task


def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = TaskForm()
    return render(request, 'add_task.html', {'task_form': task_form})

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task_form = TaskForm(instance=task)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')

    return render(request, 'add_task.html', {
        'task_form': task_form
    })

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('show_task')