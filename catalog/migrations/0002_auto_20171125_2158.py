# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена в рублях, без копеек'),
        ),
    ]
