from django.contrib import admin
from django.urls import path

# from myapp.views import saludar
from myapp import views




urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.saludar),
    path('about/',views.about)
]