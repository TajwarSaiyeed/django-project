from django.contrib.auth.views import LogoutView
from django.urls import path

from user_authentication.views import UserLoginView, UserProfileView, UserSignUpView, EditProfileView

urlpatterns = [
    path('log-in/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', UserSignUpView.as_view(), name='signup'),
    path('profile/edit-profile', EditProfileView.as_view(), name='edit_profile'),
]