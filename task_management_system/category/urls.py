from django.urls import path

from .views import add_category

urlpatterns = [
    path('add-category/', add_category, name='add_category'),
]
