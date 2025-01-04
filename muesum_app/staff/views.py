from django.shortcuts import render, get_object_or_404, redirect
from .models import Staff
from .forms import StaffForm

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff_members': staff_members})

def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff_detail.html', {'staff': staff})

def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form})

def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_form.html', {'form': form})

def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff': staff})