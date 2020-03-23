from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def registrarse(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			usuario = form.save()
			usuario.refresh_from_db()
			usuario.username = form.cleaned_data.get('username')
			usuario.password1 = form.cleaned_data.get('password1')
			usuario.perfil.apellidos = form.cleaned_data.get('apellidos')
			usuario.perfil.nombres = form.cleaned_data.get('nombres')
			usuario.perfil.carreras.set(form.cleaned_data.get('carreras'))
			if form.cleaned_data.get('imagen_perfil'):
				usuario.perfil.imagen_perfil = form.cleaned_data.get('imagen_perfil')
			usuario.perfil.bio = form.cleaned_data.get('bio')
			#usuario.perfil.imagen_perfil = form.cleaned_data.get('imagen_perfil')
			usuario.save()
			
			#usuario = form.cleaned_data.get('username')
			#messages.success(request, f'Cuenta creada para {usuario.username}')
			return redirect('login')
		

	else:
		form = UserRegisterForm()
		#return redirect('blog-home')

	return render(request, 'usuario/registrarse.html', { 'form': form })


def perfil(request):
	
	return render(request, 'usuario/perfil.html')
