from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from user_authentication.forms import UserAuthenticationForm

class UserLoginView(LoginView):
    template_name = 'user-auth.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'Login'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, f"You are now logged in as {form.cleaned_data.get('username')}")
        return super().form_valid(form)

class UserSignUpView(CreateView):
    template_name = 'user-auth.html'
    form_class = UserAuthenticationForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'Register'
        return context

    def form_valid(self, form):
        messages.info(self.request, f"Account created for {form.cleaned_data.get('username')}")
        return super().form_valid(form)

class UserProfileView(TemplateView):
    template_name = 'profile.html'

class EditProfileView(UpdateView):
    template_name = 'profile.html'