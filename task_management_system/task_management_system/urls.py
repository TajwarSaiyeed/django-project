from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='show_task'),
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]
