from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
from .models import Comentario
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
 

def index(request):
	context = {
	'posts' : Post.objects.all()
	
	}
	return render(request, 'blog/home.html' , context )

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['titulo', 'contenido', 'materia']
	
	

	def form_valid(self, form):
		fecha_creacion = datetime.date.today()
		autor = self.request.user
		form.instance.autor = autor
		return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['titulo', 'contenido', 'materia']
	def form_valid(self, form):
		fecha_creacion = datetime.date.today()
		autor = self.request.user
		form.instance.autor = autor
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.autor:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.autor:
			return True
		return False


class ComentarioCreateView(LoginRequiredMixin, CreateView):
	model = Comentario
	fields = ['contenido']
	def form_valid(self, form):
		post = Post.objects.get(pk=self.kwargs['pk'])
		fecha_creacion = datetime.date.today()
		autor = self.request.user
		form.instance.autor = autor
		form.instance.post = post
		return super().form_valid(form)