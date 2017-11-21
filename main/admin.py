from django.contrib import admin

from .models import Phone,Email,Social
# Register your models here.
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Social)
