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
            upload_to='static/img/category/',
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
       # catalog = models.ForeignKey('Catalog', related_name = 'products',blank = True)
        catalog = models.ManyToManyField(Catalog,verbose_name = "Каталог")
        name = models.CharField(max_length=300, verbose_name = "Наименование")
        slug = models.SlugField(max_length=150, verbose_name="Ссылка")
        description = models.TextField(blank=True,verbose_name='Описание')

        material = models.ForeignKey('ProductMaterial',
            related_name = 'product',
            on_delete = models.CASCADE)
        color = models.ForeignKey('ProductColor',
            related_name = 'product',
            on_delete = models.CASCADE)
        size = models.ForeignKey('ProductSize',
            related_name = 'product',
            on_delete = models.CASCADE)
        height = models.ForeignKey('ProductHeight',
            related_name = 'product',
            on_delete = models.CASCADE)
        img1 = models.ImageField(
            upload_to='static/img/products/%Y/%m/%d',
            blank=True,
            verbose_name="Изображение 1")
        img2 = models.ImageField(
            upload_to='static/img/products/%Y/%m/%d',
            blank=True,
            verbose_name="Изображение 2")
        img3 = models.ImageField(
            upload_to='static/img/products/%Y/%m/%d',
            blank=True,
            verbose_name="Изображение 3")

        price = models.PositiveIntegerField(verbose_name='Цена в рублях, без копеек')
        available = models.BooleanField(default=True,verbose_name='В наличии')
        sku = models.CharField(
            max_length = 10,
            unique = True,
            verbose_name='Артикул',
            help_text="Уникальность проверяется автоматически")

        class Meta:
            ordering = ('name',)
            verbose_name = 'Товар'
            verbose_name_plural = 'Товары'
        def __str__(self):
            return self.name


@python_2_unicode_compatible
class ProductMaterial(models.Model):
    name = models.CharField(max_length=300, verbose_name = "Материал")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Материал'
        verbose_name_plural= 'Материалы'

        def __str__(self):
            return self.name

@python_2_unicode_compatible
class ProductColor(models.Model):
    name = models.CharField(max_length=300, verbose_name = "Цвет")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Цвет'
        verbose_name_plural= 'Цвета'

        def __str__(self):
            return self.name

@python_2_unicode_compatible
class ProductSize(models.Model):
    name = models.CharField(max_length=300, verbose_name = "Размер")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Размер'
        verbose_name_plural= 'Размеры'

        def __str__(self):
            return self.name

@python_2_unicode_compatible
class ProductHeight(models.Model):
    name = models.CharField(max_length=300, verbose_name = "Рост")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Рост'
        verbose_name_plural= 'Ростовки'

        def __str__(self):
            return self.name

# ниже много говнокода не в той модели указал foreign key, нужно в самой модели Product
# @python_2_unicode_compatible
# class ProductMaterial(models.Model):
#     product = models.ForeignKey('Product',
#         related_name = 'material',
#         on_delete=models.CASCADE)
#     name = models.CharField(max_length=300, verbose_name = "Материал")

# @python_2_unicode_compatible
# class ProductColor(models.Model):
#     product = models.ForeignKey('Product',
#         related_name = 'color',
#         on_delete=models.CASCADE)
#     name = models.CharField(max_length=300, verbose_name = "Цвет")

# @python_2_unicode_compatible
# class ProductSize(models.Model):
#     product = models.ForeignKey('Product',
#         related_name = 'size',
#         on_delete=models.CASCADE)
#     name = models.CharField(max_length=300, verbose_name = "Размер")

# @python_2_unicode_compatible
# class ProductHeight(models.Model):
#     product = models.ForeignKey('Product',
#         related_name = 'height',
#         on_delete=models.CASCADE)
#     name = models.CharField(max_length=300, verbose_name = "Рост")
    
# # Нужна ли длина самой одежды?
