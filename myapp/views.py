from django.shortcuts import render

from django.http import HttpResponse
 
# Create your views here.

#Primer hola mundo
def saludar(request):
	return HttpResponse("<h1>Hello World</h1>")


def about(request):
	return HttpResponse("About")


def hola(request):
	return HttpResponse("Hola")



def hello2(request, username):
	return HttpResponse("<h1>Hola %s como estas </h1>" %username)
	# para concatenarlo lo hacemos con 
	#  %s return HttpResponse("<h1>Hola %s como estas </h1>" %username)
	print(username)
