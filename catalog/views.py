from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Catalog, Category, Product

# Create your views here.
def index(request):
    return HttpResponse('Catalog') 

def catalog_list(request,catalog_slug):
    catalogs = Catalog.objects.all()
    current_catalog = Catalog.objects.get(slug=catalog_slug)
    categorys = Category.objects.all()
    products = Product.objects.all()

    context = {'catalogs' : catalogs,
                'current_catalog' : current_catalog,
                'categorys' : categorys,
                'products' : products,
                }
    return render (request,'catalog/catalog_list.html',context)

def category_list(request,category_slug,catalog_slug):
    return HttpResponse("CATALOG: %s, CATEGORY %s " % (catalog_slug, category_slug,))
