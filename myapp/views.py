from django.shortcuts import render

from django.http import HttpResponse
 
# Create your views here.

#Primer hola mundo
def saludar(request):
	return HttpResponse("Hello World2")


def about(request):
	return HttpResponse("About")


def hola(request):
	return HttpResponse("Hola")
