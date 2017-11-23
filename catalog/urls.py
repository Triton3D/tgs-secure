
from .models import Catalog,Category,Product
from django.conf.urls import url, include
from . import views

app_name = 'catalog'
urlpatterns = [
    #url(r'^$', views.product_list, name='product_list'),
        url(r'^$',views.index,name='index'),
        url(r'^(?P<catalog_slug>[a-zA-Z]+)/$',views.catalog_list,name='catalog_list'),
        url(r'^(?P<catalog_slug>[a-zA-Z]+)/(?P<category_slug>[a-zA-Z]+)/$',views.category_list,name='category_list'),
        ]
#ex: some url example
#url ???, views.
# # ex: /polls/
# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
# # ex: /polls/5/results/
# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
# # ex: /polls/5/vote/
# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
                                                
