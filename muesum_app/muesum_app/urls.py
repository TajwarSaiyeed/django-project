from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exhibition.urls')),
    path('professors/', include('professor.urls')),
    path('visitor/', include('visitor.urls')),
    path('staff/', include('staff.urls')),
    path('sections/', include('section.urls')),
]
