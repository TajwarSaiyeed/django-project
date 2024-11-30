from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.shortcuts import render, redirect

from first_app.forms import RegisterForm, UserChange


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('profile')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Account created for {form.cleaned_data.get("username")}')
            # messages.info(request, f'Account created for {form.cleaned_data.get("username")}')
            # messages.warning(request, f'Account created for {form.cleaned_data.get("username")}')
            # messages.error(request, f'Account created for {form.cleaned_data.get("username")}')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'sign-up.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('profile')
    elif request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            userpass = form.cleaned_data.get('password')
            # check user in the database
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = UserChange(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, f'Account Updated Successfully')
            form.save()
    else:
        form = UserChange(instance=request.user)
    return render(request, 'profile.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('login')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request=request, user=request.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change_form.html', {'form': form})

def change_password_without_old(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request=request, user=request.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'password_change_form.html', {'form': form})

