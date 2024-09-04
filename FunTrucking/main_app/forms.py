from django import forms
from .models import fueltype
from datetime import date

class fueltypeForm(forms.ModelForm):
    class Meta:
        model = fueltype
        fields = ['date', 'fuel']
        widgets = {
            'date': forms.DateInput(
            format=('%m/%d/%Y'),
             attrs={
                    'placeholder': 'Select a date',
                    'type': 'date',
                    'min': date.today().strftime('%Y-%m-%d')
                }
            ),
        }
