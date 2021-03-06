# Generated by Django 3.1 on 2021-12-09 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0003_auto_20211201_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(verbose_name='Fecha de Emision')),
                ('amount', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='customers.cliente', verbose_name='Cliente')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
