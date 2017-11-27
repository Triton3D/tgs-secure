from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Catalog, Category, Product


def catalog_list(request,catalog_slug):
    catalog_list = Catalog.objects.all()
    current_catalog = Catalog.objects.get(slug=catalog_slug)
    categorys = Category.objects.all() #change to category_list
    products = Product.objects.all() #change to product_list

    context = {'catalog_list' : catalog_list,
                'current_catalog' : current_catalog,
                'categorys' : categorys,
                'products' : products,
                }
    return render (request,'catalog/catalog_list.html',context)

def category_list(request,category_slug,catalog_slug):
    catalog_list = Catalog.objects.all()
    current_catalog = Catalog.objects.get(slug=catalog_slug) #change to try
    current_category = Category.objects.get(slug=category_slug) #change to try
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    filtered_product_list = Product.objects.all().filter(category__slug=category_slug)
    
    context = {'catalog_list' : catalog_list,
                'current_catalog' : current_catalog,
                'current_category' : current_category,
                'category_list' : category_list,
                'product_list' : product_list,
                'filtered_product_list' : filtered_product_list,
                }
    return render (request,'catalog/category_list.html',context)
    #return HttpResponse("CATALOG: %s, CATEGORY %s " % (catalog_slug, category_slug,))

def product_card(request,catalog_slug,category_slug,product_slug):
    catalog_list = Catalog.objects.all()
    current_product = Product.objects.get(slug=product_slug)
    categorys = Category.objects.all() #change to category_list
    products = Product.objects.all() #change to product_list

    context = {'catalog_list' : catalog_list,
                'current_product' : current_product,
                'categorys' : categorys,
                'products' : products,
                }
    return render (request,'catalog/product_card.html',context)

# def category_list(request,catalog_slug):
#     catalog = Catalog.objects.get(slug=catalog_slug)
#     category_list = Category.objects.get(catalog=catalog.name)
#     # product = Product.objects.get(catalog=catalog.name)
#     context = {'catalog': catalog,'category_list' : category_list,}
#     #'product' : product,
#     return render(request,'catalog/category_list.html',context)

# def product_list(request,category_slug):
#     category = Category.objects.get(slug=category_slug)
#     product_list = Product.objects.get(category=category.name)
#     context = {'category' : category,'product_list' : product_list,}
#     return render(request,'catalog/product.html',context)

# def product(request,product_slug):
#     product = Product.objects.get(slug=product_slug)
#     context = {
#     'product' : product,}
#     return render(request,'catalog/product.html',context)

##Rustam tested this and it was bad idea <<<<<<<<<<<<<<<<<<<
# def catalogs(request):
#     catalog_list = Catalog.objects.all()
#     categorys = Category.objects.all()
#     products = Product.objects.all()

#     context = {'catalog_list': catalog_list,
#                 'categorys' : categorys,
#                 'products' : products,
#                 }
#     return render (request,'catalog/catalog_list.html',context)
