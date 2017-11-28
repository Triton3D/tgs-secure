# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 20:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя каталога')),
                ('slug', models.SlugField(max_length=150, verbose_name='Ссылка')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание каталога')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя категории')),
                ('slug', models.SlugField(max_length=255, verbose_name='Ссылка')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание категории')),
                ('img1', models.ImageField(blank=True, upload_to='static/img/category/', verbose_name='Картинка категории')),
                ('catalog', models.ManyToManyField(to='catalog.Catalog', verbose_name='Каталог')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=150, verbose_name='Ссылка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('img1', models.ImageField(blank=True, upload_to='static/img/products/%Y/%m/%d', verbose_name='Изображение 1')),
                ('img2', models.ImageField(blank=True, upload_to='static/img/products/%Y/%m/%d', verbose_name='Изображение 2')),
                ('img3', models.ImageField(blank=True, upload_to='static/img/products/%Y/%m/%d', verbose_name='Изображение 3')),
                ('price', models.PositiveIntegerField(verbose_name='Цена в рублях, без копеек')),
                ('available', models.BooleanField(default=True, verbose_name='В наличии')),
                ('sku', models.CharField(help_text='Уникальность проверяется автоматически', max_length=10, unique=True, verbose_name='Артикул')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductHeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Рост')),
            ],
            options={
                'verbose_name': 'Рост',
                'verbose_name_plural': 'Ростовки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductColor'),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductHeight'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductMaterial'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='catalog.ProductSize'),
        ),
    ]
