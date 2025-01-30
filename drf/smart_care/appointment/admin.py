from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from . import models

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']
    def patient_name(self,obj):
        return obj.patient.user.first_name

    def doctor_name(self,obj):
        return f"Dr. {obj.doctor.user.first_name}"

    def save_model(self, request, obj, form, change):
        if obj.appointment_status == 'Running' and obj.appointment_types == "Online":
            email_subject = "Appointment Reminder"
            email_body = render_to_string('appointment_reminder.html', {
                'patient_name': obj.patient.user.first_name,
                'doctor_name': obj.doctor.user.first_name,
                'symptom': obj.symptom,
                'time': obj.time,
                'meet_link': obj.doctor.meet_link
            })
            email = EmailMultiAlternatives(
                email_subject,
                '',
                to=[obj.patient.user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(models.Appointment, AppointmentAdmin)