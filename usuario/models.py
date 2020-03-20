from django.db import models
from django.contrib.auth.models import User
from blog import models as blog_models

# Create your models here.
class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	#?nombres = models.CharField(max_length=100) 
	#?apellidos = models.CharField(max_length=100)
	#password??
	#email??
	#edad
	carreras = models.ManyToManyField(blog_models.Carrera) 
	#Posts = models.ManyToManyField(blog_models.Post) #Si lo descomento me pide posts al momento de crear perfil
	#¿Reportes? despues