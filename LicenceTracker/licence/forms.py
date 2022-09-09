from datetime import datetime
from django import forms
from .models import Licence

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateLicence(forms.ModelForm):

    class Meta:
        model = Licence
        fields = '__all__'
        widgets = {
            'purchase_date': DateInput(),
            'comment': forms.Textarea(attrs={'rows':4, 'cols':50}),
        }
        