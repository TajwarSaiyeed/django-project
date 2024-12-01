from django.shortcuts import render, redirect
from django.contrib import messages
from categories.forms import CategoryForm

def add_category(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category added successfully')
            return redirect('add_category')
    else:
        category_form = CategoryForm()
    return render(request, 'add-category.html', {
        'category_form': category_form
    })