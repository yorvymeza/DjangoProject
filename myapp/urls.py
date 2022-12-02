from django.urls import path


# Ya no tendria que darle el nombre de la carpeta
# myapp

from .  import  views
# from myapp.views import 
# El punto . es muy importante 
# para indicar que estamos en la rais de la 
# carpeta

# Recodemos que esto es una lista urlpatterns[]
urlpatterns = [

  # path('',views.saludar),
  path('about/',views.about),
  path('hola/', views.hola),
  path('hello/<str:username>', views.hello2),

  # Vamos a crear una ruta projects y tasks
  path('projects/', views.projects),
  path('tasks/', views.tasks),
  path('create_task/', views.create_task)


]