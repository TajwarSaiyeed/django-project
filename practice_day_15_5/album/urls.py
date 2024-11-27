from django.urls import path

from .views import add_album, edit_album

urlpatterns = [
    path('add-album/', add_album, name='add_album'),
    path('edit-album/<int:pk>/', edit_album, name='edit_album'),
]
