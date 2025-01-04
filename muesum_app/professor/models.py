from django.db import models

class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Professor {self.first_name} {self.last_name}"
