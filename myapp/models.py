from django.db import models

# Create your models here.

# Con esto lo que estoy haciendo es crear un tabla


class Project(models.Model):
	name = models.CharField(max_length=200)

	# Esto se lo pasamos despues 
	# El null=True es muy necesario
	price = models.FloatField(null=True)
	# Tambien he visto que usan default='anything'
	email = models.EmailField(max_length= 255, unique=True, null=True)


# Podemos crear otra clase

class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	project = models.ForeignKey(Project, on_delete=models.CASCADE)


	# Esto se lo pasamos despues
	email = models.EmailField(max_length= 255, unique=True, null=True)
	 # Es para relacionar la tabla
	 # on_delete=models.CASCADE
	 # Es para cuando se elimine un datos 
	 # Se eliminen todos lo que esten con el


