from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse('Catalog') 
def catalog_list(request,catalog_slug):
    return HttpResponse("CATALOG: %s" % catalog_slug) 
def category_list(request,category_slug,catalog_slug):
    return HttpResponse("CATALOG: %s, CATEGORY %s " % (catalog_slug, category_slug,))
def product(request,product_slug):
	product = Product.objects.get(slug=product_slug)
	context = {
	'product' : product,
	}
	return render(request,'catalog/product.html',context)
	
