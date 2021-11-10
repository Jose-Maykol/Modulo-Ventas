from django.db import models

# Create your models here.

class Cliente(models.Model):

    # TODO: Define fields here

    RUC = models.CharField(verbose_name='RUC')
    name = models.CharField(verbose_name='Nombre de cliente')
    adress = models.CharField(verbose_name='Direccion')
    city = models.CharField(verbose_name= 'Ciudad')
    phone_numer = models.CharField(verbose_name= 'Numero de telefono')
    email = models.EmailField(verbose_name='Email')
    site_web = models.URLField(verbose_name= 'Sitio web', blank= True)

    class Meta:

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

