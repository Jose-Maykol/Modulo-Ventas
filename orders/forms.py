from django import forms
from django.forms import widgets
from .models import Pedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = (
            'customer',
            'product',
            'amount',
            'order_status',
            'order_date'
        ) 
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}),
            'order_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
