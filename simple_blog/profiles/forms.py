from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        help_texts = {
            'name': 'Enter the name of the profile',
            'about': 'Enter a brief description of the profile',
            'author': 'Select the author of the profile',
        }
        error_messages = {
            'name': {
                'required': 'Please enter the name of the profile',
            },
            'about': {
                'required': 'Please enter a brief description of the profile',
            },
            'author': {
                'required': 'Please select the author of the profile',
            },
        }
