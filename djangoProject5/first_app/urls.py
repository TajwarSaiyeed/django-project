from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='first_app_home'),
    path('form/', views.form, name='first_app_form'),
    path('django_form/', views.django_form, name='first_app_django_form'),
    path('django_form/', views.student_form, name='first_app_django_form'),
    path('django_form/', views.user_form, name='first_app_django_form'),
    path('django_form/', views.password_validator, name='first_app_django_form'),
]
