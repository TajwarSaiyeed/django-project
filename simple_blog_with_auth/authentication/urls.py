from django.urls import path
from .views import sign_up, log_in, profile, log_out, password_reset, edit_profile, UserLoginView

from django.contrib.auth.views import LogoutView
from django.contrib import messages


urlpatterns = [
    path('sign-up/', sign_up, name='signup'),
    # path('log-in/', log_in, name='login'),
    path('log-in/', UserLoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/edit-profile', edit_profile, name='edit_profile'),
    path('password-reset/', password_reset, name='password_reset'),
    # path('logout/', log_out, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
