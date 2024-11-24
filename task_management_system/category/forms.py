from .models import Category
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        help_texts = {
            'category_name': 'Enter the category name',
        }
        error_messages = {
            'category_name': {
                'required': "Category name is required",
                'unique': "Category name already exists",
                'max_length': "Category name should be less than 100 characters"
            }
        }


