# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_auto_20171126_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/banners/'),
        ),
    ]