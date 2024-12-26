from django.urls import path
from .views import AddMusicianView, EditMusiciansView, DeleteMusicianView

urlpatterns = [
    path('add-musician/', AddMusicianView.as_view(), name='add_musician'),
    path('edit-musician/<int:pk>/', EditMusiciansView.as_view(), name='edit_musician'),
    path('delete-musician/<int:pk>/', DeleteMusicianView.as_view(), name='delete_musician'),
]
