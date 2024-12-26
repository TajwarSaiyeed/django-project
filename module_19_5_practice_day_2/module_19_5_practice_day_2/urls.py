from django.urls import path, include
from django.contrib import admin
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('', include('user_authentication.urls')),
]
