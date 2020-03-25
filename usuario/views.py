from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
			
			return redirect('login')
			#return render(request, 'login.html' , context)
		

	else:
		form = UserRegisterForm()
		#return redirect('blog-home')

	return render(request, 'usuario/registrarse.html', { 'form': form, 'title': "Registrarse" })


def perfil(request):
	
	return render(request, 'usuario/perfil.html')

class EliminarUsuario(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
	model = User
	success_url = reverse_lazy('blog-home')
	template_name = 'usuario/user_confirm_delete.html'
	def test_func(self):
		usuario = self.get_object()
		if self.request.user == usuario:
			return True
		return False
	def get_object(self):
		#u = self.get_object()
    	#user = get_object_or_404(User, username = self.kwargs.get('usuario'))
    	#return User.objects.filter(username=user)
		return self.request.user
        #return get_object_or_404(User, self.kwargs.get('username'))