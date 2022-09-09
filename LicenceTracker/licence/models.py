from typing_extensions import Required
from django.db import models

# Create your models here.
class LicenceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LicenceStatus(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Licence(models.Model):
    licence_type = models.ForeignKey("LicenceType", on_delete=models.CASCADE, null=True)
    created_by = models.CharField(max_length=50, default='Guest')
    comment = models.TextField(max_length=500)
    status = models.ForeignKey("LicenceStatus", on_delete=models.CASCADE, null=True)
    purchase_date = models.DateField()
    request_number = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    available_for_reallocation = models.BooleanField(default= False)

    def __str__(self):
        return '{0} - {1}'.format(self.created_by, self.licence_type.name)

