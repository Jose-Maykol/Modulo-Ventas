from django.db import models
from customers.models import Cliente
from products.models import Producto

# Create your models here.

class Venta(models.Model):

    class PaymentStatus(models.TextChoices):
        pending = 'PENDIENTE', 'Pendiente'
        defeated = 'VENCIDO' , 'Vencido'
        paid =  'PAGADO' , 'Pagado'

    class SaleStatus(models.TextChoices):
        completed = 'COMPLETADO' , 'Completado'
        pending =  'PENDIENTE' , 'Pendiente'
       

    customer = models.OneToOneField(Cliente, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Cliente')
    product = models.OneToOneField(Producto, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Producto')
    amount = models.PositiveIntegerField(verbose_name= 'Cantidad') 
    payment_status = models.CharField(max_length= 50,choices= PaymentStatus.choices, verbose_name= 'Estado de pago')
    sale_status = models.CharField(max_length= 50,choices= SaleStatus.choices, verbose_name= 'Estado de venta')
    sale_date = models.DateTimeField(verbose_name= 'Fecha de venta')

    class Meta:

        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
