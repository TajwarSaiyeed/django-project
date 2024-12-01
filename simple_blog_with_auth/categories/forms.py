from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        help_texts = {
            'name': 'Enter the name of the category',
        }
        error_messages = {
            'name': {
                'required': 'Please enter the name of the category',
            },
        }