# Define database models (tables, columns)

from django.db import models

# Create your models here.

class UserCities(models.Model):
    city_name=models.CharField(max_length=100)
    def __str__(self):
        return self.city_name
