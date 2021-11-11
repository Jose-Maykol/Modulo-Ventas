from django import forms
from django.forms import widgets
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = (
            'RUC',
            'DNI',
            'name',
            'adress',
            'city',
            'phone_number',
            'email',
            'site_web'
        ) 
        widgets = {
            'RUC': forms.TextInput(attrs={'class': 'form-control'}),
            'DNI': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'site_web': forms.TextInput(attrs={'class': 'form-control'}),
        }
