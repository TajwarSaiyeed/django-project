from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='first_app_home'),
]