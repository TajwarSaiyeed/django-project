from django.urls import path
from .views import sign_up, log_in, profile, home, log_out, change_password, change_password_without_old

urlpatterns = [
    path('', home, name='home'),
    path('sign-up/', sign_up, name='sign_up'),
    path('login/', log_in, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', log_out, name='logout'),
    path('change-password/', change_password, name='change_password'),
    path('change-password-without_old/', change_password_without_old, name='change_password_without_old'),
]