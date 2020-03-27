
from django.urls import path
from django.urls import include, path

from usuario import views as usuario_views 

from django.contrib.auth import views as auth_views

urlpatterns = [

    
    path('login/', auth_views.LoginView.as_view(template_name = 'usuario/login.html'), name= "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'usuario/logout.html'), name= "logout"),

    path('registrarse/', usuario_views.registrarse, name= "registrarse"),

    path('perfil/', usuario_views.perfil, name= "perfil"),
    path('perfildeotro/<int:pk>', usuario_views.PerfilDeOtro.as_view(), name= "perfil-de-otro"),
    path('perfil/eliminar/', usuario_views.EliminarUsuario.as_view(), name= "eliminar-usuario")
]
