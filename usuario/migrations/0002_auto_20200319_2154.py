# Generated by Django 3.0.4 on 2020-03-19 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='carrera',
            new_name='carreras',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='Posts',
        ),
    ]
