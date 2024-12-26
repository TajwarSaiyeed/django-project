from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from user_authentication.models import RegisterForm

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Logged In Successfully")
        return super().form_valid(form)
