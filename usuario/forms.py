##Aqui es donde hice el retroceso :(
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from blog.models import Carrera
#from django.core.validators import MaxValueValidator, MinValueValidators


class UserRegisterForm(UserCreationForm):
	
	edad = forms.IntegerField()
	apellidos = forms.CharField(max_length=100)
	carreras = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all()) 
	#authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
	#imagen_perfil = forms.ImageField()

	nombres = forms.CharField(max_length=100) 


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'apellidos' , 'nombres' , 'edad', 'carreras', ) 

