from django.urls import path

from .views import add_musician, edit_musician, delete_musician

urlpatterns = [
    path('add-musician/', add_musician, name='add_musician'),
    path('edit-musician/<int:pk>/', edit_musician, name='edit_musician'),
    path('delete-musician/<int:pk>/', delete_musician, name='delete_musician'),
]
