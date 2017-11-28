# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductColor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductHeight'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductMaterial'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductSize'),
        ),
    ]