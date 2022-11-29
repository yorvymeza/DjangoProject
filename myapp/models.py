from django.db import models

# Create your models here.

# Con esto lo que estoy haciendo es crear un tabla


class Project(models.Model):
	name = models.CharField(max_length=200)


# Podemos crear otra clase

class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	 # Es para relacionar la tabla
	 # on_delete=models.CASCADE
	 # Es para cuando se elimine un datos 
	 # Se eliminen todos lo que esten con el


