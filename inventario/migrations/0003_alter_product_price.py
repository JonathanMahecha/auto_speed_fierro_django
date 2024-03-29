# Generated by Django 5.0.2 on 2024-03-15 01:20

import django.core.validators
import inventario.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_garantias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[inventario.models.validate_not_zero, django.core.validators.MinValueValidator(0)], verbose_name='Precio'),
        ),
    ]
