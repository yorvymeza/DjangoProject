from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

# from django.http import HttpResponse, JsonResponse
# JsonResponse Para que el navegador pueda reconocerlo

# Vamos import los modelos para hacer una consulta
from .models import Project, Task
 
# Create your views here.

#Primer hola mundo
# def saludar(request):
# 	return HttpResponse("<h1>Hello World</h1>")


def about(request):
	return HttpResponse("About")


def hola(request):
	return HttpResponse("Hola")



def hello2(request, username):
	return HttpResponse("<h1>Hola %s como estas </h1>" %username)
	# para concatenarlo lo hacemos con 
	#  %s return HttpResponse("<h1>Hola %s como estas </h1>" %username)
	print(username)

	# De esta forma nosotros tenemos un parametros que podemos ir cambiando
	# y ir visitando otra


def projects(request):
	# Esto es un queryset
	# projects = list(Project.objects.all())
	# Esto es porque esto llamando todo loo datos
	# Yo solo quiero los valores
	projects = list(Project.objects.values())

	return JsonResponse(projects, safe=False)


	# return HttpResponse('projects')


def tasks(request):
	return HttpResponse('tasks')



def create_task(request):
	return HttpResponse('create_task.html')
