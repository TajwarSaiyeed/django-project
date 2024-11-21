from django import forms

from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        help_texts = {
            'name': 'Enter the name of the author',
            'bio': 'Enter a brief bio of the author',
            'phone_no': 'Enter the phone number of the author',
        }
        error_messages = {
            'name': {
                'required': 'Please enter the name of the author',
            },
            'bio': {
                'required': 'Please enter a brief bio of the author',
            },
            'phone_no': {
                'required': 'Please enter the phone number of the author',
            },
        }
