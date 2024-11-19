from django.http import HttpResponse
from django.shortcuts import render, redirect

from first_app import models


def home(request):
    students = models.Student.objects.all()
    return render(request, 'home.html', {
        'students': students
    })

def delete_student(request, roll):
    student = models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')