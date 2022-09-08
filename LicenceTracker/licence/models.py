from django.db import models

# Create your models here.
class LicenceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Licence(models.Model):
    licence_type = models.ForeignKey(LicenceType, on_delete=models.CASCADE, null=True)
    created_by = models.CharField(max_length=50, default='Guest')
    comment = models.TextField()

    def __str__(self):
        return self.name

