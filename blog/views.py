from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
	context = {
	'posts' : Post.objects.all()
	
	}
	return render(request, 'blog/home.html' , context )

class PostDetailView(DetailView):
	model = Post

