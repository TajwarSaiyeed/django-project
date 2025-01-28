from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # custormize the queryset
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        doctor_id = self.request.query_params.get('doctor_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        elif doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        else:
            queryset = queryset.all()
        return queryset


