# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Catalog(models.Model):
        name = models.CharField(max_length=255)
        slug = models.SlugField(max_length=150)
        description = models.TextField()

        class Meta:
            ordering = ('name',)

        def __str__(self):
            return self.name


@python_2_unicode_compatible
class Product(models.Model):
        name = models.CharField(max_length=300)
        slug = models.SlugField(max_length=150)
        description = models.TextField()
        manufacturer = models.CharField(max_length=300, blank=True)
        price = models.DecimalField(max_digits=8, decimal_places=2)
        available = models.BooleanField(default=True)

        class Meta:
            ordering = ('name',)

        def __str__(self):
            return self.name

@python_2_unicode_compatible
class Category(models.Model):
        name = models.CharField(max_length=255)
        slug = models.SlugField(max_length=255)
        description = models.TextField(blank=True)
        catalog = models.ManyToManyField(Catalog)

        class Meta:
            ordering = ('name',)

        def __str__(self):
            return self.name
