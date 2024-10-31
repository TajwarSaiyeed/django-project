from django.shortcuts import render
import datetime

def home(request):
    d = {"author": "Abid", "age": 20, 'list': [1, 2, 3, 4, 5], 'courses': [
        {'name': 'Python', 'duration': '3 months'},
        {'name': 'Django', 'duration': '2 months'},
        {'name': 'React', 'duration': '1 months'},
    ], 'list_of_strings': ['python', 'is', 'awesome'], 'date': datetime.datetime.now(), 'val':"This is a value"}
    return render(request, 'home.html', d)