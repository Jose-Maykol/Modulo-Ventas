# Generated by Django 3.1 on 2021-12-02 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20211201_1912'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('order_status', models.CharField(choices=[('COMPLETADO', 'Completado'), ('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado')], max_length=50, verbose_name='Estado de pedido')),
                ('order_date', models.DateTimeField(verbose_name='Fecha de pedido')),
                ('customer', models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='customers.cliente', verbose_name='Cliente')),
                ('product', models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]