from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        help_texts = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Enter your email',
            'phone_number': 'Enter your phone number',
            'instrument_type': 'Enter your instrument type',
        }
