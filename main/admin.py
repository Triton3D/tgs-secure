from django.contrib import admin

from .models import Phone,Email,Social,Menu
# Register your models here.
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Social)
admin.site.register(Menu)
