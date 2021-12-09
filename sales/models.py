from django.db import models
from customers.models import Cliente
from products.models import Producto

# Create your models here.

class Venta(models.Model):

    class PaymentStatus(models.TextChoices):
        pending = 'PENDIENTE', 'Pendiente'
        defeated = 'VENCIDO' , 'Vencido'
        paid =  'PAGADO' , 'Pagado'

    class BillStatus(models.TextChoices):
        completed = 'FACTURADO' , 'Facturado'
        pending =  'NO FACTURADO' , 'No Facturado'
       

    customer = models.ForeignKey(Cliente, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Cliente')
    product = models.ForeignKey(Producto, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Producto')
    amount = models.PositiveIntegerField(verbose_name= 'Cantidad') 
    payment_status = models.CharField(max_length= 15,choices= PaymentStatus.choices, verbose_name= 'Estado de pago')
    bill_status = models.CharField(max_length= 15,choices= BillStatus.choices, verbose_name= 'Estado de factura')
    sale_date = models.DateTimeField(verbose_name= 'Fecha de venta')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return str(self.product)