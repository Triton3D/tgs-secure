# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from ckeditor.fields import RichTextField


@python_2_unicode_compatible
class Catalog(models.Model):
        name = models.CharField(max_length=255,verbose_name="Имя каталога")
        slug = models.SlugField(max_length=150,verbose_name="Ссылка")
        description = RichTextField(blank=True,verbose_name="Описание каталога")

        class Meta:
            ordering = ('name',)
            verbose_name = 'Каталог'
            verbose_name_plural = 'Каталоги'
                        
        def __str__(self):
            return self.name


@python_2_unicode_compatible
class Category(models.Model):
        name = models.CharField(max_length=255, verbose_name = "Имя категории")
        slug = models.SlugField(max_length=255, verbose_name = "Ссылка")
        description = RichTextField(blank=True, verbose_name = "Описание категории")
        catalog = models.ManyToManyField(Catalog,verbose_name = "Каталог")
        img1 = models.ImageField(
            upload_to='img/catalog/',
            blank=True,
            verbose_name="Картинка категории")
            
        class Meta:
            ordering = ('name',)
            verbose_name = 'Категория товара'
            verbose_name_plural = 'Категории товаров'
        def __str__(self):
            return self.name

@python_2_unicode_compatible
class Product(models.Model):
        category = models.ForeignKey('Category', related_name = 'products')
        name = models.CharField(max_length=300, verbose_name = "Наименование")
        slug = models.SlugField(max_length=150, verbose_name="Ссылка")
        description = models.TextField(blank=True,verbose_name='Описание')
        img1 = models.ImageField(upload_to='img/products/%Y/%m/%d', blank=True, verbose_name="Изображение 1")
        img2 = models.ImageField(upload_to='img/products/%Y/%m/%d', blank=True, verbose_name="Изображение 2")
        img3 = models.ImageField(upload_to='img/products/%Y/%m/%d', blank=True, verbose_name="Изображение 3")
        price = models.PositiveIntegerField(verbose_name='Цена в рублях, без копеек')
        available = models.BooleanField(default=True,verbose_name='В наличии')
        sku = models.CharField(max_length = 10, verbose_name='Артикул')
#        catalog = models.ManyToManyField(Catalog, verbose_name = "Каталог") 
#           category = models.ManyToManyField(Category, verbose_name = "Категория") 

        class Meta:
            ordering = ('name',)
            verbose_name = 'Товар'
            verbose_name_plural = 'Товары'
        def __str__(self):
            return self.name