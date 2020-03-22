
from django.urls import path
from django.urls import include, path

from .views import Registrarse

from django.contrib.auth import views as auth_views

urlpatterns = [

    
    path('login/', auth_views.LoginView.as_view(template_name = 'usuario/login.html'), name= "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'usuario/logout.html'), name= "logout"),

    path('registrarse/', Registrarse, name= "registrarse")
]
