from django.db import models
from customers.models import Cliente
from sales.models import Venta
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 

# Create your models here.

class Factura(models.Model):

       
    #user = models.ForeignKey(User, on_delete= models.SET_DEFAULT, default= None)
    customer = models.ForeignKey(Cliente, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Cliente')
    RUC = models.CharField(max_length= 12,verbose_name='RUC', default= None, blank= True)
    phone_number = models.CharField(max_length= 9,verbose_name= 'Numero de telefono', default= None, blank= True)
    email = models.EmailField(verbose_name='Email', default= None, blank= True)
    issue_date = models.DateTimeField(auto_now_add= True,verbose_name= 'Fecha de Emision')
    sale = models.ManyToManyField(Venta, default= None)
    total = models.DecimalField(decimal_places= 2, max_digits= 10, default= 0,verbose_name= "Total", blank= True)
    
    class Meta:

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return str(self.customer)

@receiver(post_save, sender=Factura) 
def calculate_total(sender, instance, **kwargs):
    print('Esta es la factura')
    print(instance.sale.all())
    if instance.total == 0:
        for sale in instance.sale.all():
            instance.total += sale.product.price * sale.amount
            sale = Venta.objects.get(id = sale.id)
            sale.bill_status = 'FACTURADO'
            sale.save()
        instance.save()
        

@receiver(post_save, sender=Factura) 
def pre_save_factura(sender, instance, **kwargs):
    if instance.RUC=='' and instance.phone_number=='' and instance.email=='':
        instance.RUC = instance.customer.RUC
        instance.phone_number = instance.customer.phone_number
        instance.email = instance.customer.email
        instance.save()
