from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        help_texts = {
            'title': 'Enter the title of the post',
            'content': 'Enter the content of the post',
            'category': 'Select the category of the post',
            'author': 'Select the author of the post',
        }
        error_messages = {
            'title': {
                'required': 'Please enter the title of the post',
            },
            'content': {
                'required': 'Please enter the content of the post',
            },
            'category': {
                'required': 'Please select the category of the post',
            },
            'author': {
                'required': 'Please select the author of the post',
            },
        }