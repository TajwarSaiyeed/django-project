from django.shortcuts import render
from musician.models import Musician

def home(request):
    musicians = Musician.objects.all()
    return render(request, 'home.html', {'musicians': musicians})