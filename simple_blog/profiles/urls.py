from django.urls import path

from profiles import views

urlpatterns = [
    path('add/', views.add_profile, name="add_profile"),
]
