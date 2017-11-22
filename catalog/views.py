from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Catalog') 
def catalog_list(request,catalog_slug):
    return HttpResponse("CATALOG: %s" % catalog_slug) 
def category_list(request,category_slug,catalog_slug):
    return HttpResponse("CATALOG: %s, CATEGORY %s " % (catalog_slug, category_slug,))
