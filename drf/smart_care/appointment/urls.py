from rest_framework.routers import DefaultRouter
from .views import AppointmentViewset
from django.urls import include, path

router = DefaultRouter()

router.register(r'', AppointmentViewset)

urlpatterns = [
    path('', include(router.urls)),
]