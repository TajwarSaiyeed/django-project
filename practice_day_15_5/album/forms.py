from django import forms

from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['release_date']
        error_messages = {
            'album_name': {
                'required': "Please enter the album name",
            },
            'rating': {
                'required': "Please enter the rating",
            },
        }
