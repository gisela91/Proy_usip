# Generated by Django 4.1.1 on 2022-10-07 21:53

import almacenes.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0012_remove_ofertas_description_ofertas_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofertas',
            name='fechaInicio',
            field=models.DateField(validators=[almacenes.validators.validar_fechaInicio_oferta]),
        ),
        migrations.AlterField(
            model_name='ofertas',
            name='tipo',
            field=models.CharField(choices=[('dosxuno', '2 x 1'), ('unoregalo', 'Un set de regalo'), ('diezporciento', '10 % de rebaja')], default='dosxuno', max_length=30),
        ),
        migrations.AlterField(
            model_name='pedidoproveedor',
            name='cantidad',
            field=models.IntegerField(default=0, validators=[almacenes.validators.validar_cantidad_pedido]),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nomProveedor',
            field=models.CharField(max_length=100, unique=True, validators=[almacenes.validators.validar_nombre_proveedor]),
        ),
    ]