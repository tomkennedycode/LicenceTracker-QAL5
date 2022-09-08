from django.contrib import admin
from .models import Licence, LicenceType

# Register your models here.
admin.site.register(Licence)
admin.site.register(LicenceType)