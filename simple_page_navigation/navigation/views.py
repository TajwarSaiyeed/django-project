from django.http import HttpResponse
from django.shortcuts import render

def about(req):
    return render(req, "navigation/about.html")

def contact(req):
    return render(req, "navigation/contact.html")