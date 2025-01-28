from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer


class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer