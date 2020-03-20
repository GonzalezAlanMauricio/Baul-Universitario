from django.contrib import admin
from .models import Post, Comentario, Materia, Carrera


admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Carrera)
admin.site.register(Materia)

# Register your models here.
