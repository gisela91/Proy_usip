# Generated by Django 4.1.1 on 2022-10-05 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0011_ofertas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ofertas',
            name='description',
        ),
        migrations.AddField(
            model_name='ofertas',
            name='tipo',
            field=models.CharField(choices=[('dosxuno', '2 x 1'), ('unoregalo', 'Un set de regalo'), ('diezporciento', '10 % de rebaja')], default='-------', max_length=30),
        ),
    ]
