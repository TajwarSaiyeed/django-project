from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.CharField(max_length=10, default="Rahim")

    def __str__(self):
        return f"{self.name} - {self.roll}"
