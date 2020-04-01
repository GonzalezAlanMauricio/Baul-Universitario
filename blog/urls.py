from django.urls import path
from blog.views import (PostDetailView, 
						PostUpdateView, 
						PostCreateView, 
						PostDeleteView, 
						ComentarioCreateView, 
						ComentarioDeleteView,
						HomePostDetailView,
                        Inicio
						)

from . import views

urlpatterns = [
    path('', Inicio.as_view(), name='blog-inicio'),
    path('inicio/', HomePostDetailView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/actualizar/', PostUpdateView.as_view(), name='post-actualizar'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post-eliminar'),
    path('post/<int:pk>/agregar_comentario/', ComentarioCreateView.as_view(), name='post-agregar-comentario'),
    path('post/<int:pk>/eliminar_comentario/', ComentarioDeleteView.as_view(), name='eliminarComentario'),
    path('post/nuevo/', PostCreateView.as_view(), name='post-nuevo'),
]