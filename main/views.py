from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Phone, Email,Social,Menu

def fill_db(request):
	if not Phone.objects.get(name = "Основной"):
		try:
			phone = Phone(name="Основной",number="8 351 025 02 02")
		except Error:
			pass
		else:
			phone.save()
	if not Email.objects.get(name = "Основной"):
		try:
			email = Email(name="Основной",email="test@test.ru")
		except Error:
			pass
		else:
			email.save()
	
	try:
		social = Social(name="Facebook",enabled=True)
	except Error:
		pass
	else:
		social.save()
	return HttpResponse("OK!")