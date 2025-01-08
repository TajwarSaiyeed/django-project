from django.db import models

from car_brand.models import CarBrand


class Car(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name