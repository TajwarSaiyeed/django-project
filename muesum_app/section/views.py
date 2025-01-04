from django.shortcuts import render, get_object_or_404, redirect
from .models import Section
from .forms import SectionForm

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'section_list.html', {'sections': sections})

def section_detail(request, pk):
    section = get_object_or_404(Section, pk=pk)
    section.increment_visitor_count()
    return render(request, 'section_detail.html', {'section': section})

def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'section_form.html', {'form': form})

def section_edit(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm(instance=section)
    return render(request, 'section_form.html', {'form': form})

def section_delete(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        section.delete()
        return redirect('section_list')
    return render(request, 'section_confirm_delete.html', {'section': section})