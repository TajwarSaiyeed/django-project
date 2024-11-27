from django.shortcuts import render, redirect

from .forms import AlbumForm
from .models import Album


def add_album(request):
    if request.method == 'POST':
        album = AlbumForm(request.POST)
        if album.is_valid():
            album.save()
    else:
        album = AlbumForm()
    return render(request, 'add_album.html', {'album': album})


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album = AlbumForm(request.POST, instance=album)
        if album.is_valid():
            album.save()
            return redirect('home')
    else:
        album = AlbumForm(instance=album)
    return render(request, 'add_album.html', {'album': album})
