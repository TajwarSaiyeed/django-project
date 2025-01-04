
from django.urls import path
from .views import section_list, section_detail, section_create, section_edit, section_delete

urlpatterns = [
    path('', section_list, name='section_list'),
    path('<int:pk>/', section_detail, name='section_detail'),
    path('add/', section_create, name='section_create'),
    path('<int:pk>/edit/', section_edit, name='section_edit'),
    path('<int:pk>/delete/', section_delete, name='section_delete'),
]