# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20171123_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['order_p'], 'verbose_name': 'пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
    ]