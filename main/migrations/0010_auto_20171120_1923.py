# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_social'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Социальную сеть', 'verbose_name_plural': 'Социальная сеть'},
        ),
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(choices=[('https://facebook.com', 'Facebook'), ('https://vk.com', 'VK'), ('https://instagram.com', 'Instagram')], max_length=60),
        ),
    ]