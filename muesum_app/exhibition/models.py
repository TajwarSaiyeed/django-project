from django.db import models
from section.models import Section

class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='exhibitions')

    def __str__(self):
        return self.title
