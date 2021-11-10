from django.db import models

# Create your models here.

class Producto(models.Model):
    """Model definition for Producto."""

    # TODO: Define fields here

    class TypesTaxes(models.TextChoices):
        IGV = 'IGV', 'IGV'

    name = models.CharField(max_length= 200, verbose_name= 'Nombre del producto')
    price = models.PositiveIntegerField(verbose_name='Precio')
    cost = models.PositiveIntegerField(verbose_name= 'Coste')
    taxe = models.CharField(verbose_name= 'Impuesto', choices= TypesTaxes.choices)
    #category = models.CharField(verbose_name= 'Categorias')
    image =  models.ImageField(upload_to= 'img/productos')
    class Meta:

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

