##Aqui es donde hice el retroceso :(
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil
from blog.models import Carrera


class SignUpForm(UserCreationForm):
	
	fecha_nacimiento = forms.DateTimeField()
	apellidos = forms.CharField(max_length=100)
	carreras = forms.ModelMultipleChoiceField(queryset=Carrera.objects.all()) 
	#authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

	nombres = forms.CharField(max_length=100) 

	# def __init__ (self, *args, **kwargs):
	# 	#brand = kwargs.pop("brand")
	# 	super(SignUpForm, self).__init__(*args, **kwargs)
	# 	self.fields["carreras"].widget = forms.widgets.CheckboxSelectMultiple()
	# 	self.fields["carreras"].help_text = ""
	# 	self.fields["carreras"].queryset = Carrera.objects.all()

	class Meta:
		model = User
		fields = ('username', 'apellidos' , 'nombres' , 'fecha_nacimiento', 'password1', 'password2', 'carreras',) 

