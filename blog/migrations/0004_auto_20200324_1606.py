# Generated by Django 3.0.4 on 2020-03-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200322_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tipo',
            field=models.CharField(choices=[('Solicitud de apunte digital', 'S Ap D'), ('Solicitud de apunte fisico', 'S Ap F'), ('Solicitud de otros materiales', 'S O M'), ('Solicitud de ayuda ', 'S A'), ('Recomendacion', 'Recom'), ('Donacion de apunte digital', 'D Ap D'), ('Donacion de apunte fisico', 'D Ap F'), ('Donacion de otros materiales', 'D O M')], default='Recomendacion', max_length=29),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='comentario_pics'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='comentario_pics'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='comentario_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen1',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='post_pics'),
        ),
    ]
