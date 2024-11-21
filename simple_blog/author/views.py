from django.shortcuts import render, redirect

from .forms import AuthorForm


def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = AuthorForm()
    return render(request, 'add_author.html', {
        'author_form': author_form
    })
