
from .models import Catalog,Category,Product
from django.conf.urls import url, include
from . import views

app_name = 'catalog'
urlpatterns = [
            #    url(r'^$', views.product_list, name='product_list'),
                url(r'^$',views.catalog_list,name='catalog_list'),
                url(r'^(?P<catalog_slug>[a-zA-Z]+)/$',views.catalog_list,name='category_list'),
                url(r'^(?P<category_slug>[a-zA-Z]+)/$',views.category_list,name='product_list'),
                url(r'^(?P<product_slug>[a-zA-Z])/$',views.product,name='product'),
                ]
                   
                                                
