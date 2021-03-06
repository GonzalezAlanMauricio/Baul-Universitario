##Aqui es donde hice el retroceso :(
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from blog.models import Carrera
#from django.core.validators import MaxValueValidator, MinValueValidators


class UserRegisterForm(UserCreationForm):
	
	edad = forms.IntegerField(required= False)
	apellidos = forms.CharField(max_length=100)
	carreras = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all()) 
	
	imagen_perfil = forms.ImageField(required = False)

	nombres = forms.CharField(max_length=100) 

	bio = forms.CharField(required=False, max_length = 500, help_text="Escribi algo sobre vos",widget=forms.Textarea)


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email' ,'apellidos' , 'nombres' , 'edad', 'carreras', 'imagen_perfil',  ) 

