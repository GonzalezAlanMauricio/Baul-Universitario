from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
	#Post va a tener un id autoincremental generado por Django
	contenido = models.TextField()
	titulo = models.CharField(max_length = 1000) 
	#imagen1
	#imagen2
	#imagen3
	fecha_creacion = models.DateTimeField(default = timezone.now)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	materia = models.ForeignKey('Materia', on_delete=models.CASCADE)
	#comentarios = models.ManyToManyField('Comentario') Si lo descomento al momento de crear un post me pide comentarios
	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	#Comentario va a tener un id autoincremental generado por Django
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	contenido = models.TextField(default = 'Escribe un comentario')
	post = models.ForeignKey('Post', on_delete = models.CASCADE)
	#imagen1
	#imagen2
	#imagen3
	def __str__(self):
		return self.contenido

class Carrera(models.Model):
	#Carrera va a tener un id autoincremental generado por Django
	nombre = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre
	

class Materia(models.Model):
	#Materia va a tener un id autoincremental generado por Django
	nombre = models.CharField(max_length=100) 
	anio = models.DateTimeField(default = timezone.now)
	carreras = models.ManyToManyField('Carrera')

	def __str__(self):
		return self.nombre