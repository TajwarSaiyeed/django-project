from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.first_app_home),
]
