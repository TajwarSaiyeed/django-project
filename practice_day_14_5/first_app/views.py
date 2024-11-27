from django.shortcuts import render

from first_app.forms import InputFrom,GeeksModelForm


def home(request):
    if request.method == "POST":
        form = InputFrom(request.POST)
        if form.is_valid():
            print("Validation Success!", form.cleaned_data)
    else:
        form = InputFrom()
    return render(request, 'index.html', {'form': form})

def model_form(request):
    if request.method == "POST":
        form = GeeksModelForm(request.POST)
        if form.is_valid():
            print("Validation Success!", form.cleaned_data)
    else:
        form = GeeksModelForm()
    return render(request, 'model_form.html', {'form': form})