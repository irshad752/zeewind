# forms.py
from django import forms
from .models import WarrantyRegistration

class WarrantyRegistrationForm(forms.ModelForm):
    class Meta:
        model = WarrantyRegistration
        fields = [
            'product_name', 'product_color', 'name', 'phone',
            'email', 'address', 'serial_number', 'date_of_purchase'
        ]
        widgets = {
            'date_of_purchase': forms.DateInput(attrs={'type': 'date'}),
        }
