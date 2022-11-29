from django.contrib import admin
from django.urls import path, include

# from myapp.views import saludar
# from myapp import views

# Debemos añadir include 

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('',views.saludar),
    # path('about/',views.about)
 
    # De esta forma se esta incluyendo las rutas
    path('', include('myapp.urls'))
]