# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-19 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_bestseller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Rolex', 'Rolex'), ('Timex', 'Timex'), ('Ted Baker', 'Ted Baker'), ('Tissot', 'Tissot'), ('Michael Kors', 'Michael Kors'), ('Lacoste', 'Lacoste'), ('Lotus', 'Lotus'), ('Citizen', 'Citizen')], default='Rolex', max_length=20),
        ),
    ]
