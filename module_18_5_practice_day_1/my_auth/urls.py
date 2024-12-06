from django.urls import path
from .views import user_register, user_login, user_logout, user_profile, user_change_password, user_change_password_without_old

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('change-password-with-old/', user_change_password, name='change_password'),
    path('change-password-without-old/', user_change_password_without_old, name='change_password_without_old'),
]