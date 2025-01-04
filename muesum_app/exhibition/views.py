from django.shortcuts import render, redirect, get_object_or_404
from .models import Exhibition
from .forms import ExhibitionForm

def exhibition_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'exhibition_list.html', {'exhibitions': exhibitions})

def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    return render(request, 'exhibition_detail.html', {'exhibition': exhibition})

def exhibition_create(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhibition_list')
    else:
        form = ExhibitionForm()
    return render(request, 'exhibition_form.html', {'form': form})

def exhibition_edit(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, instance=exhibition)
        if form.is_valid():
            form.save()
            return redirect('exhibition_list')
    else:
        form = ExhibitionForm(instance=exhibition)
    return render(request, 'exhibition_form.html', {'form': form})

def exhibition_delete(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    if request.method == 'POST':
        exhibition.delete()
        return redirect('exhibition_list')
    return render(request, 'exhibition_confirm_delete.html', {'exhibition': exhibition})