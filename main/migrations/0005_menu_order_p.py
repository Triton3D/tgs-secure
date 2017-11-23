# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_menu_order_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='order_p',
            field=models.PositiveIntegerField(choices=[('0', 'Первая позиция'), ('1', 'Вторая позиция'), ('2', 'Третья позиция'), ('3', 'Четвертая позиция'), ('4', 'Пятая позиция'), ('5', 'Шестая позиция')], default=0, help_text='Первая позиция - крайняя левая, Шестая - крайняя правая', unique=True, verbose_name='Позиция пункта в меню'),
        ),
    ]
