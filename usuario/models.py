from django.db import models
from django.contrib.auth.models import User
from blog import models as blog_models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


# Create your models here.
class Perfil(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	imagen_perfil = models.ImageField(default = 'default.jpg', upload_to = 'perfil_pics')
	nombres = models.CharField(max_length=100) 
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField(        
		default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)])
	carreras = models.ManyToManyField(blog_models.Carrera)
	bio = models.TextField(max_length = 500) 
	#¿Reportes? despues
	def __str__(self):
		return f'Perfil de {self.usuario.username}'
	

	def save(self , *args, **kwargs):
		super().save()

		img = Image.open(self.imagen_perfil.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.imagen_perfil.path)