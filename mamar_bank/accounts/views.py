from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout

from accounts.forms import UserRegistrationForm, UserUpdateForm, PasswordChangeForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone


def send_password_change_mail(user, mail_subject, template_name):
    message_body = render_to_string(template_name, {
        'user': user,
        'timestamp': timezone.now(),
    })

    email = EmailMultiAlternatives(
        mail_subject,
        '',
        '',
        [user.email],
    )
    email.attach_alternative(message_body, "text/html")
    email.send()
    return email



class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


class UserBankAccountUpdateView(LoginRequiredMixin, View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
    
class UserPasswordChangeView(LoginRequiredMixin,View):
    template_name = "password-change.html"
    
    def get(self, request):
        form = PasswordChangeForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.user.username, password=form.cleaned_data.get('old_password'))
            if user:
                user.set_password(form.cleaned_data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                
                
                send_password_change_mail(user, 'Password Changed', 'password-change-email.html')
                
                messages.success(request, "Password changed successfully!")
                return redirect('profile')
            else:
                form.add_error('old_password', 'Please enter a valid old password')
                return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})
