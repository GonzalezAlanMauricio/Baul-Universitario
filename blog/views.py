from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
	context = {
	'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html' , context )
