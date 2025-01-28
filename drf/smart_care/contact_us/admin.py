from django.contrib import admin

from contact_us.models import ContactUs

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'problem']

admin.site.register(ContactUs, ContactModelAdmin)