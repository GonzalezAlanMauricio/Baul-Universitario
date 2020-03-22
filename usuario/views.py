from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def Registrarse(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			usuario = form.cleaned_data.get('username')
			messages.success(request, f'Cuenta creada para {usuario}')
			return redirect('login')

	else:
		form = UserCreationForm()

	return render(request, 'usuario/registrarse.html', { 'form': form })