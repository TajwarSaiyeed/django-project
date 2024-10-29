from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("This is first_app home page")

def courses(request):
    return HttpResponse("This is courses page")