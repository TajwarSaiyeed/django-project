from django.urls import include, path
from rest_framework.routers import DefaultRouter

from service.views import ServiceViewset

router = DefaultRouter()

router.register(r'', ServiceViewset)

urlpatterns = [
    path('', include(router.urls)),
]