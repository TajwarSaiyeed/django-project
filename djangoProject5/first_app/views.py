from django.shortcuts import render
from .forms import ContactForm, StudentData, UserForm, PasswordValidationProject


def home(request):
    return render(request, 'home.html')


def form(request):
    # print(request.POST)
    return render(request, 'form.html')


def django_form(request):
    # form = ContactForm(request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    # return render(request, 'django_form.html', {
    #     'form': form
    # })

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data.get('file')
            # my_photo = form.cleaned_data.get('my_photo')
            # # print(file)
            # print(form.cleaned_data)
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            #
            # with open('./first_app/upload/' + my_photo.name, 'wb+') as destination:
            #     for chunk in my_photo.chunks():
            #         destination.write(chunk)

            return render(request, 'django_form.html', {
                'form': form
            })
    else:
        # print(form.errors)
        form = ContactForm()

    return render(request, 'django_form.html', {
        'form': form
    })


def student_form(request):
    if request.method == "POST":
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()

    return render(request, 'django_form.html', {
        'form': form
    })


def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = UserForm()

    return render(request, 'django_form.html', {
        'form': form
    })


def password_validator(request):
    if request.method == "POST":
        form = PasswordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()

    return render(request, 'django_form.html', {
        'form': form
    })
