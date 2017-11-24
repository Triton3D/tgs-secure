from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Catalog,Category

# Create your views here.
def catalog_list(request):
	catalog_list = Catalog.objects.all()
	# product = Product.objects.all()
	context = {
	'catalog_list': catalog_list,
	# 'product' : product,
	}
	return render(request,'catalog/index.html',context)

def category_list(request,catalog_slug):
	catalog = Catalog.objects.get(slug=catalog_slug)
	category_list = Category.objects.get(catalog=catalog.name)
	# product = Product.objects.get(catalog=catalog.name)
	context = {'catalog': catalog,'category_list' : category_list,}
	#'product' : product,
	return render(request,'catalog/category_list.html',context)

def product_list(request,category_slug):
	category = Category.objects.get(slug=category_slug)
	product_list = Product.objects.get(category=category.name)
	context = {'category' : category,'product_list' : product_list,}
	return render(request,'catalog/product.html',context)

def product(request,product_slug):
	product = Product.objects.get(slug=product_slug)
	context = {
	'product' : product,}
	return render(request,'catalog/product.html',context)
		
