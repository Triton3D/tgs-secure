from django.db import models

class Banner(models.Model):
    styles = (
        ('style_11','Стиль 1: Большой баннер с непрозрачным блоком (560х360)'),
        ('style_12','Стиль 2: Большой баннер с прозрачным блоком (560х360)'),
        ('style_21','Стиль 3: Маленький вертикальный баннер с заголовком внизу (270х360)'),
        ('style_22','Стиль 4: Маленький вертикальный баннер с заголовком вверху (270х360)'),
        )
    
    name = models.CharField(max_length = 255,
                            unique=True,
                            default = 'Главный баннер',
                            verbose_name = "Уникальное название баннера",
                            )
    subtitle = models.CharField(max_length = 14,
                            default = 'Подзаголовок',
                            verbose_name = "Подзаголовок",
                            help_text = "",
                            blank = True)
    title1 = models.CharField(max_length = 15,
                            default = 'Заголовок в', 
                            verbose_name = "Первая строка заголовка",
                            help_text = "Верхняя строка заголовка (15 символов)",
                            blank = True)

    title2 = models.CharField(max_length = 15,
                            default = 'две строки', 
                            verbose_name = "Вторая строка заголовка",
                            help_text = "Нижняя строка заголовка (15 символов)",
                            blank = True)

    button_text = models.CharField(max_length = 30,
                            default = 'Подробности',
                            verbose_name = "Текст на кнопке",
                            help_text = "Макс. 30 символов",
                            blank = True)
    url = models.CharField(max_length=255,
                            default = '#', 
                            verbose_name = "Ссылка",
                            help_text = 'Относительная ссылка на товар, католог, акцию и прочее (например "catalog/women")',
                            blank = True)
    style = models.CharField(max_length=255,
                            default = 'Стиль 1', 
                            verbose_name = "Стиль",
                            help_text = "Выберете один из 4-х видов баннера",
                            blank = True,
                            choices = styles)

    img = models.ImageField(upload_to = 'static/img/banners/',
                            blank = False,
                            unique = True,
                            verbose_name = "Изображение на баннере",
                            help_text = "Размер изображения баннера выбирать в пропорции выбранного стиля") 


    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ('id',)

    def __str__(self):
        return self.name

