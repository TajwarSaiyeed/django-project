from django.urls import path

from album.views import AddAlbumView, EditAlbumView

urlpatterns = [
    path('add-album/', AddAlbumView.as_view(), name='add_album'),
    path('edit-album/<int:pk>/', EditAlbumView.as_view(), name='edit_album'),
]