from rest_framework import viewsets
from . import serializers
from .models import ContactUs

class ContactusViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer