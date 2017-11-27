"""tgs URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/',include('catalog.urls')), 
    url(r'^main/',include('main.urls'))
]
