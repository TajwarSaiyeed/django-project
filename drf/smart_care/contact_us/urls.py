from django.urls import include, path
from rest_framework.routers import DefaultRouter

from contact_us.views import ContactusViewset

router = DefaultRouter()

router.register(r'', ContactusViewset)

urlpatterns = [
    path('', include(router.urls)),
]