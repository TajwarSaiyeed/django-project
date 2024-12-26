from django.db import models

from musician.models import Musician


class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name="albums")
    album_name = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    rating = models.CharField(
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        ],
        max_length=1
    )

    def __str__(self):
        return f"{self.album_name}-{self.musician.first_name}-{self.musician.last_name}"