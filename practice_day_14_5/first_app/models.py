from django.db import models
from django.core import validators


class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    time_field = models.TimeField(auto_now=False, auto_now_add=False)
    url_field = models.URLField(max_length = 200)
    uuid_field = models.UUIDField()
    positive_integer_field = models.PositiveIntegerField()
    json_field = models.JSONField()

    def __str__(self):
        return self.title