# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-23 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourites',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]