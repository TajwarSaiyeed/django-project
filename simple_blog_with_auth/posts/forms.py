from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        help_texts = {
            'title': 'Enter the title of the post',
            'content': 'Enter the content of the post',
            'category': 'Select the category of the post',
            'image': 'Upload an image for the post',
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
            'image': {
                'required': 'Please upload an image for the post',
            },
        }