from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

Fuels = (
    ('D', 'Diesel'),
    ('G', 'Gasoline'),
    ('E', 'Electric'),
    ('H', 'Hybrid'),
)

class Truck(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('truck-detail', kwargs={'truck_id': self.id})

class fueltype(models.Model):
    date = models.DateField('Fuel date')
    fuel = models.CharField(
        max_length=1,
        choices=Fuels,
        default=Fuels[0][0]
    )

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_fuel_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']