from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name', 'phone', 'email', 'sender_email',
            'legal_business_name', 'country_region', 'address',
            'apartment_suite', 'city', 'state', 'pin_code',
            'timezone', 'unit_system', 'weight_unit', 'currency',
            'order_prefix', 'order_suffix'
        ]
