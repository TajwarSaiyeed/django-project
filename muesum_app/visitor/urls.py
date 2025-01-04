from django.urls import path
from .views import (
    visitor_list, visitor_detail, visitor_create, visitor_edit, visitor_delete
)

urlpatterns = [
    path('', visitor_list, name='visitor_list'),
    path('<int:pk>/', visitor_detail, name='visitor_detail'),
    path('add/', visitor_create, name='visitor_create'),
    path('<int:pk>/edit/', visitor_edit, name='visitor_edit'),
    path('<int:pk>/delete/', visitor_delete, name='visitor_delete'),
]
