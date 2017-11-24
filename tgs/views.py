from django.shortcuts import render
from main.models import Phone,Email,Social,Menu
from catalog.models import Catalog, Category, Product

def home(request):
    phone = Phone.objects.get(name="Основной") #Maybe use TRY: construction and disable name changing
    email = Email.objects.get(name="Основной")#Maybe use TRY: construction and disable name changing
    social_list = Social.objects.all()
    catalog_list = Catalog.objects.all()
    menu_items = Menu.objects.all()
    context = {
            'phone': phone,
            'email': email,
            'social_list': social_list,
            'catalog_list': catalog_list,
            'menu_items': menu_items,
            }
    return render(request,
                'tgs/index.html'
                ,context)
