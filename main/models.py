from django.db import models
from django.core.validators import RegexValidator,EmailValidator
# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=255, default='Номер телефона 1',unique=True,verbose_name="Название",help_text="")
    number = models.CharField(max_length=15,unique=True,verbose_name="Номер телефона",help_text="Введите номер телефона используя следующий формат: +Х(ХХХ)ХХХ-ХХ-ХХ или X XXX XXX XX XX ",validators=[RegexValidator(regex=r'^(\+\d{1}|\d)(\ \d{3}\ |\(\d{3}\))(\d{3}\-\d{2}\-\d{2}|\d{3}\ \d{2}\ \d{2})$',)])
    link = models.CharField(max_length=255,default="tel:",verbose_name="Ссылка",help_text="")
    class Meta:
        verbose_name = 'номер телефона'
        verbose_name_plural = 'Номера телефонов'

    def __str__(self):
        return self.name

class Email(models.Model):
    name = models.CharField(max_length=255, default='Адрес электронной почты 1',unique=True,verbose_name="Название")
    email = models.CharField(max_length=255,unique=True,verbose_name="Адрес электронной почты (e-mail)",validators=[EmailValidator()])
    link = models.CharField(max_length=255,default="mailto:",verbose_name="Ссылка")
    class Meta:
        verbose_name = 'Адрес электронной почты'
        verbose_name_plural = 'Адреса электронной почты'

    def __str__(self):
        return self.name

class Social(models.Model):
    SOCIAL_LIST = (
            ('Facebook','Facebook'),
            ('VK','VK'),
            ('Instagram','Instagram'),
           # ('Odnoklassniki','Odnoklassniki'),
            ('Twitter','Twitter'),
            )
    name = models.CharField(max_length=60,choices=SOCIAL_LIST,verbose_name="Социальная сеть")
    enabled = models.BooleanField(verbose_name="Отображать на страницах сайта?")
    link = models.CharField(max_length=255,verbose_name="Аккаунт")
    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = 'Социальная сеть'
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=20,verbose_name="Пункт меню")
    enabled = models.BooleanField(verbose_name="Отображать в меню")
    link = models.CharField(max_length=255,verbose_name="Ссылка на страницу")
    class Meta:
        verbose_name = 'Пункты меню'
        verbose_name_plural = 'Пункт меню'
    def __str__(self):
        return self.name
