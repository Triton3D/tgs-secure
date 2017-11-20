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
        return self.name+": "+self.number

class Email(models.Model):
    name = models.CharField(max_length=255, default='Адрес электронной почты 1',unique=True,verbose_name="Название")
    email = models.CharField(max_length=255,unique=True,verbose_name="Адрес электронной почты (e-mail)",validators=[EmailValidator()])
    link = models.CharField(max_length=255,default="mailto:",verbose_name="Ссылка")
    class Meta:
        verbose_name = 'Адрес электронной почты'
        verbose_name_plural = 'Адреса электронной почты'

    def __str__(self):
        return self.name+": "+self.email

#class Social(models.Model):
#    fb_available = models.
