from django import forms
from django.forms import widgets
from .models import Venta

class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = (
            'customer',
            'product',
            'amount',
            'payment_status',
            'sale_status',
            'sale_date'
        ) 
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_status': forms.Select(attrs={'class': 'form-control'}),
            'sale_status': forms.Select(attrs={'class': 'form-control'}),
            'sale_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
