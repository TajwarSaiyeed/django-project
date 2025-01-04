from django.shortcuts import render, get_object_or_404, redirect
from .models import Visitor
from .forms import VisitorForm


def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitor_list.html', {'visitors': visitors})

def visitor_detail(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    return render(request, 'visitor_detail.html', {'visitor': visitor})

def visitor_create(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm()
    return render(request, 'visitor_form.html', {'form': form})

def visitor_edit(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'visitor_form.html', {'form': form})

def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitor_list')
    return render(request, 'visitor_confirm_delete.html', {'visitor': visitor})