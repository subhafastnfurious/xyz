from django.db import models

# Create your models here.
class VehicleBrand(models.Model):
    description = models.CharField(max_length=100)


    def __str__(self):              # __unicode__ on Python 2
        return self.description

class VehicleModel(models.Model):
    description = models.CharField(max_length=100)
    brand = models.ForeignKey(VehicleBrand)