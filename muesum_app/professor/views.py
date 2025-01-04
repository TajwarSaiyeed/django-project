from django.shortcuts import render, get_object_or_404, redirect
from .models import Professor
from .forms import ProfessorForm


def professor_list(request):
    professors = Professor.objects.all()
    return render(request, 'professor_list.html', {'professors': professors})

def professor_detail(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    return render(request, 'professor_detail.html', {'professor': professor})

def professor_create(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
    return render(request, 'professor_form.html', {'form': form})

def professor_edit(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'professor_form.html', {'form': form})

def professor_delete(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('professor_list')
    return render(request, 'professor_confirm_delete.html', {'professor': professor})