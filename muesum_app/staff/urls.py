from django.urls import path
from .views import staff_list, staff_detail, staff_create, staff_edit, staff_delete

urlpatterns = [
    path('', staff_list, name='staff_list'),
    path('<int:pk>/', staff_detail, name='staff_detail'),
    path('add/', staff_create, name='staff_create'),
    path('<int:pk>/edit/', staff_edit, name='staff_edit'),
    path('<int:pk>/delete/', staff_delete, name='staff_delete'),
]