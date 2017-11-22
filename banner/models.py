from django.db import models
#img1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

class Banner(models.Model):
    text1 = models.CharField(max_length = 255,
                            default = 'Заголовок1', # user uppercase in template
                            verbose_name = "Заголовок1",
                            help_text = "some help text here",
                            blank = True)

    text2 = models.CharField(max_length = 255,
                            default = 'Заголовок2', # user uppercase in template
                            verbose_name = "Заголовок2",
                            help_text = "some help text here",
                            blank = True)

    button_text = models.CharField(max_length = 255,
                            default = 'Текст на кнопке', # use uppercase in template
                            verbose_name = "Текст на кнопке",
                            help_text = "help text ",
                            blank = True)

    banner_img = models.ImageField(upload_to = 'products/%Y/%m/%d', blank=True)