# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(default='Баннер№№. Заголовок1', help_text='some help text here', max_length=255, verbose_name='Баннер1. Заголовок1')),
                ('text2', models.CharField(default='Банер№№. Заголовок2', help_text='some help text here', max_length=255, verbose_name='Баннер1. Заголовок2')),
                ('button_text', models.CharField(default='Банер№№. Текст на кнопке', help_text='show more  ', max_length=255, verbose_name='Баннер1. Текст на кнопке')),
            ],
        ),
    ]
