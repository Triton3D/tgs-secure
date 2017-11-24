# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20171122_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.PositiveIntegerField(default=12425, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='В наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена'),
        ),
    ]
