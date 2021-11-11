from django.db import models

# Create your models here.

class Cliente(models.Model):

    # TODO: Define fields here

    RUC = models.CharField(max_length= 12,verbose_name='RUC')
    DNI = models.CharField(max_length= 8,verbose_name= "DNI")
    name = models.CharField(max_length= 50,verbose_name='Nombre de cliente')
    adress = models.CharField(max_length= 50,verbose_name='Direccion')
    city = models.CharField(max_length= 50,verbose_name= 'Ciudad')
    phone_number = models.CharField(max_length= 9,verbose_name= 'Numero de telefono')
    email = models.EmailField(verbose_name='Email')
    site_web = models.URLField(verbose_name= 'Sitio web', blank= True)

    class Meta:

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
