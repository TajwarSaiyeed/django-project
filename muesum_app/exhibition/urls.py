from django.urls import path
from .views import exhibition_list, exhibition_detail, exhibition_create, exhibition_edit, exhibition_delete

urlpatterns = [
    path('', exhibition_list, name='exhibition_list'),
    path('<int:pk>/', exhibition_detail, name='exhibition_detail'),
    path('add/', exhibition_create, name='exhibition_create'),
    path('<int:pk>/edit/', exhibition_edit, name='exhibition_edit'),
    path('<int:pk>/delete/', exhibition_delete, name='exhibition_delete'),
]