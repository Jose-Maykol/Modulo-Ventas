from django import forms
from django.forms import models, widgets
from .models import Factura

class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura
        fields = (
            'customer',
            'sale',
        ) 
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'sale': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        #self.fields['sale'].queryset = models.Factura.objects.filter(id =1)
    
