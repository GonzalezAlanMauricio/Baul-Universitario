from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
	#Post va a tener un id autoincremental generado por Django
	contenido = models.TextField()
	titulo = models.CharField(max_length = 1000) 
	imagen1 = models.ImageField( upload_to = 'post_pics' , null=True, blank=True)
	imagen2 = models.ImageField( upload_to = 'post_pics' ,null=True, blank=True)
	imagen3 = models.ImageField( upload_to = 'post_pics' , null=True, blank=True)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	materia = models.ForeignKey('Materia', on_delete=models.CASCADE)


	tiposDePost =[

		 ('Solicitud de apunte digital', 'Solicitud de apunte digital'),
		 ('Solicitud de apunte fisico', 'Solicitud de apunte fisico'),
		 ('Solicitud de otros materiales', 'Solicitud de otros materiales'),
		 ('Solicitud de ayuda ', 'Solicitud de ayuda '),

		 ('Recomendacion', 'Recomendacion'),
		 ('Donacion de apunte digital', 'Donacion de apunte digital'),
		 ('Donacion de apunte fisico', 'Donacion de apunte fisico'),
		 ('Donacion de otros materiales', 'Donacion de otros materiales'),
		
	]
		
	
		



	tipo = models.CharField(
		max_length = 29,
		choices= tiposDePost ,
		default= tiposDePost[5]
	)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


class Comentario(models.Model):
	#Comentario va a tener un id autoincremental generado por Django
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_creacion = models.DateTimeField(default = timezone.now)
	contenido = models.TextField(default = 'Escribe un comentario')
	post = models.ForeignKey('Post', on_delete = models.CASCADE)
	imagen1 = models.ImageField( null=True, blank=True, upload_to = 'comentario_pics')
	imagen2 = models.ImageField( null=True, blank=True, upload_to = 'comentario_pics')
	imagen3 = models.ImageField( null=True, blank=True, upload_to = 'comentario_pics')
	def __str__(self):
		return self.contenido
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.post.pk})

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