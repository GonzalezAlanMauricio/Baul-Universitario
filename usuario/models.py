from django.db import models
from django.contrib.auth.models import User
from blog import models as blog_models

from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	nombres = models.CharField(max_length=100) 
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField(        
		default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
	carreras = models.ManyToManyField(blog_models.Carrera)
	info = models.TextField(max_length = 500) 
	#¿Reportes? despues
	def __str__(self):
		return f'Perfil de {self.usuario.username}'