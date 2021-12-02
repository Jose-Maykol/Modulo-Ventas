from django.db import models

# Create your models here.

class Producto(models.Model):

    name = models.CharField(max_length= 100, verbose_name= 'Nombre del producto')
    price = models.DecimalField(decimal_places= 2, max_digits= 10 ,verbose_name='Precio')
    cost = models.DecimalField(decimal_places= 2, max_digits= 10 ,verbose_name= 'Coste')
    image =  models.ImageField(upload_to= 'img/productos', null = True, blank = True, verbose_name= 'Imagen')
    description = models.TextField(max_length=100, verbose_name= 'Descripcion')

    class Meta:

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
