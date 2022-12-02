from django.contrib import admin
from django.urls import path, include

# from myapp.views import saludar
from myapp import views

# from .views  import HomeView 
# Debemos añadir include 

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('',views.saludar),
    # path('about/',views.about)

    # path('',HomeView.as_view(), name='home')
 
    # De esta forma se esta incluyendo las rutas
    path('',include('myapp.urls'))
]