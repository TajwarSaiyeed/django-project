from django.contrib import admin
from django.urls import path, include
from car.views import CarListView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarListView.as_view(), name='home'),
    path('', include('user_authentication.urls')),
    path('car/', include('car.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)