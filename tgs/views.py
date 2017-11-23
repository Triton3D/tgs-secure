from django.shortcuts import render
from main.models import Phone,Email,Social
from catalog.models import Catalog, Category, Product
def home(request):
    phone = Phone.objects.get(name="Основной")
    email = Email.objects.get(name="Основной")
    social_list = Social.objects.all()
    catalog_list = Catalog.objects.all()
    
    context = {
            'phone': phone,
            'email': email,
            'social_list': social_list,
            'catalog_list': catalog_list,
            }
    return render(request,
                'tgs/index.html'
                ,context)
