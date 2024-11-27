from django.shortcuts import render, redirect

from .forms import MusicianForm
from .models import Musician


def add_musician(request):
    if request.method == 'POST':
        musician = MusicianForm(request.POST)
        if musician.is_valid():
            musician.save()

    else:
        musician = MusicianForm()
    return render(request, 'add_musician.html', {'musician': musician})


def edit_musician(request, pk):
    musician = Musician.objects.get(pk=pk)
    if request.method == 'POST':
        musician = MusicianForm(request.POST, instance=musician)
        if musician.is_valid():
            musician.save()
            return redirect('home')
    else:
        musician = MusicianForm(instance=musician)
    return render(request, 'add_musician.html', {'musician': musician})


def delete_musician(request, pk):
    musician = Musician.objects.get(pk=pk)
    musician.delete()
    return redirect('home')
