from django.shortcuts import render

from first_app.forms import StudentModelForm


def home(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentModelForm()
    return render(request, 'home.html', {
        'form': form
    })
