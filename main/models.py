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
        verbose_name = 'адрес электронной почты'
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
        verbose_name = 'аккаунт социальной сети'
        verbose_name_plural = 'Социальные сети'
    def __str__(self):
        return self.name

class Menu(models.Model):
    MENU_POSITION = (
        (0,'Первая'),
        (1,'Вторая'),
        (2,'Третья'),
        (3,'Четвертая'),
        (4,'Пятая'),
        (5,'Шестая'),
        (6,'Седьмая'),)
    name = models.CharField(max_length=20,verbose_name="Пункт меню")
    order_p = models.PositiveIntegerField(default=0,unique=True,choices=MENU_POSITION,verbose_name="Позиция пункта в меню",help_text="Первая позиция - крайняя левая, Шестая - крайняя правая",)
    enabled = models.BooleanField(verbose_name="Отображать в меню")
    link = models.CharField(max_length=255,verbose_name="Ссылка на страницу",validators=[RegexValidator(regex=r'^((([a-z]|[0-9])+|([a-z]|\_)+)|\/)+$')],help_text="")
    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order_p']
    def __str__(self):
#        return self.name
        return str(self.order_p+1)+": "+self.name
