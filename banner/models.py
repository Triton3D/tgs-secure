from django.db import models

class Banner(models.Model):
    text1 = models.CharField(max_length=255,
                            default='Баннер№№. Заголовок1', # user uppercase in template
                            verbose_name="Баннер1. Заголовок1",
                            help_text="some help text here")

    text2 = models.CharField(max_length=255,
                            default='Банер№№. Заголовок2', # user uppercase in template
                            verbose_name="Баннер1. Заголовок2",
                            help_text="some help text here")

    button_text = models.CharField(max_length=255,
                            default='Банер№№. Текст на кнопке', # use uppercase in template
                            verbose_name="Баннер1. Текст на кнопке",
                            help_text="show more  ") #use uppercase in template
