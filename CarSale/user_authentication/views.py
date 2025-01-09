from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from user_authentication.forms import UserAuthenticationForm, UserUpdate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from order.models import Order


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


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'Profile'

        orders = Order.objects.filter(user=self.request.user)
        context['orders'] = orders
        return context


@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = UserUpdate
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_type'] = 'Edit Profile'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(self.success_url)
        else:
            messages.error(request, 'There was an error updating your profile')
            return self.form_invalid(form)
