from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    visitor_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def increment_visitor_count(self):
        self.visitor_count += 1
        self.save()