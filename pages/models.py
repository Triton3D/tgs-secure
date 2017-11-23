from django.db import models
from ckeditor.fields import RichTextField

class Pages(models.Model):
	name = models.CharField(max_length=50,verbose_name="Имя страницы")
	title = models.CharField(max_length=255,verbose_name="Заголовок страницы")
	content = RichTextField(verbose_name="Содержимое страницы")	
	class Meta:
		verbose_name = "страница"
		verbose_name_plural = "Страницы"
	def __str__(self):
		return self.name

