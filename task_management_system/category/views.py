from django.shortcuts import render, redirect

from category.forms import CategoryForm


def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = CategoryForm()

    return render(request, 'add_category.html', {'category_form': category_form})
