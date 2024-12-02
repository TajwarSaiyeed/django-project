from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

from authentication.forms import UserAuthenticationForm, UserUpdate, PasswordUpdate


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = UserAuthenticationForm()
    return render(request, 'sign-up.html', {'form': form})

def log_in(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'log-in.html', {'form': form})

@login_required
def log_out(request):
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdate(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = UserUpdate(instance=request.user)
    return render(request, 'profile.html', {'form': form, 'type': 'Edit Profile'})

@login_required
def profile(request):
    my_posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {
        'my_posts': my_posts,
        'type' : 'Profile'
    })

@login_required
def password_reset(request):
    if request.method == 'POST':
        form = PasswordUpdate(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password updated successfully')
            return redirect('profile')
    else:
        form = PasswordUpdate(user=request.user)
    return render(request, 'profile.html', {'form': form, 'type': 'Change Password'})
