from django.db import models
from django.contrib.auth.models import User
from blog import models as blog_models

# Create your models here.
class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	nombres = models.CharField(max_length=100) 
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField()
	carreras = models.ManyToManyField(blog_models.Carrera)
	info = models.TextField(max_length = 500) 
	#¿Reportes? despues