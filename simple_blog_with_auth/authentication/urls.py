from django.urls import path
from .views import sign_up, log_in, profile, log_out

urlpatterns = [
    path('sign-up/', sign_up, name='signup'),
    path('log-in/', log_in, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', log_out, name='logout'),
]
