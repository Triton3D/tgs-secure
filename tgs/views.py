from django.shortcuts import render, get_object_or_404
from main.models import Phone,Email,Social,Menu
from catalog.models import Catalog, Category, Product

def home(request):
    #phone = Phone.objects.get(name="Основной") #Maybe use TRY: construction and disable name changing
    phone = get_object_or_404(Phone, name="Основной")
    #email = Email.objects.get(name="Основной")#Maybe use TRY: construction and disable name changing
    email = get_object_or_404(Email, name="Основной")#Maybe use TRY: construction and disable name changing
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

#https://docs.djangoproject.com/en/1.11/intro/tutorial03/
# def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})