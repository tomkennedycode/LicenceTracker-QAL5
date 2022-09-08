from django import forms
from .models import Licence

class CreateLicence(forms.ModelForm):

    class Meta:
        model = Licence
        fields = '__all__'
        