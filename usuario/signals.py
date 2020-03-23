from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender = User)
def update_profile_signal(sender, instance, created, **kwargs):
	if created:
		Perfil.objects.create(usuario=instance)
	instance.perfil.save()

@receiver(post_save, sender = User)
def save_perfil(sender, instance,  **kwargs):
	
	instance.perfil.save() 
