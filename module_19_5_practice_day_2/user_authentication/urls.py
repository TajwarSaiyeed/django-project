from django.urls import path
from .views import user_register, UserLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]