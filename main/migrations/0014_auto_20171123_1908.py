# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20171123_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['order_p'], 'verbose_name': 'пункт меню', 'verbose_name_plural': 'Пункты меню'},
        ),
        migrations.AddField(
            model_name='menu',
            name='order_p',
            field=models.PositiveIntegerField(choices=[(0, 'Первая'), (1, 'Вторая'), (2, 'Третья'), (3, 'Четвертая'), (4, 'Пятая'), (5, 'Шестая'), (6, 'Седьмая')], default=0, help_text='Первая позиция - крайняя левая, Шестая - крайняя правая', unique=True, verbose_name='Позиция пункта в меню'),
        ),
    ]
