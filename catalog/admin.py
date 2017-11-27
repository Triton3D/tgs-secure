from django.contrib import admin
from .models import Catalog,Product,Category

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','category','slug','price','available','sku')
#	list_display = ('first_name', 'last_name')
admin.site.register(Catalog)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)


