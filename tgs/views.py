from django.shortcuts import render
from main.models import Phone,Email
def home(request):
    phone = Phone.objects.get(name="Основной")
    email = Email.objects.get(name="Основной")
    context = {
            'phone': phone,
            'email': email,
            }
    return render(request,'tgs/index.html',context)
