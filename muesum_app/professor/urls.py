from django.urls import path
from .views import professor_list, professor_detail, professor_create, professor_edit, professor_delete

urlpatterns = [
# # Professor URLs
    path('', professor_list, name='professor_list'),
    path('<int:pk>/', professor_detail, name='professor_detail'),
    path('add/', professor_create, name='professor_create'),
    path('<int:pk>/edit/', professor_edit, name='professor_edit'),
    path('<int:pk>/delete/', professor_delete, name='professor_delete'),
]