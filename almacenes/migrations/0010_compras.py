# Generated by Django 4.1.1 on 2022-10-05 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0009_pedidoproveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedproveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.pedidoproveedor')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.producto')),
            ],
        ),
    ]