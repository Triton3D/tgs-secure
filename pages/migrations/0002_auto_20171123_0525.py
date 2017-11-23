# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 05:25
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'verbose_name': 'страницу', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterField(
            model_name='pages',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Содержимое страницы'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя страницы'),
        ),
    ]