from django.db import models
from customers.models import Cliente
from products.models import Producto
from sales.models import Venta
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Pedido(models.Model):

    class OrderStatus(models.TextChoices):
        completed = 'COMPLETADO' , 'Completado'
        pending =  'PENDIENTE' , 'Pendiente'
        cancelled= 'CANCELADO', 'Cancelado'
       

    customer = models.ForeignKey(Cliente, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Cliente')
    product = models.ForeignKey(Producto, on_delete= models.SET_DEFAULT, default= None, verbose_name= 'Producto')
    amount = models.PositiveIntegerField(verbose_name= 'Cantidad') 
    order_status = models.CharField(max_length= 50,choices= OrderStatus.choices, verbose_name= 'Estado de pedido')
    order_date = models.DateTimeField(verbose_name= 'Fecha de pedido')
    class Meta:

        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

@receiver(post_save, sender=Pedido)
def generateSale(sender, instance, **kwargs):
    if instance.order_status == 'COMPLETADO':
        venta = Venta.objects.create(
            customer = instance.customer,
            product = instance.product,
            amount = instance.amount,
            payment_status = 'PENDIENTE',
            sale_date = instance.order_date
        )
        venta.save()
        print('Se creo la venta c: !!!')

    
