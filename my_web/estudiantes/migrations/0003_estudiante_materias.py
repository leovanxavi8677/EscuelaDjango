# Generated by Django 2.2.7 on 2019-11-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
        ('estudiantes', '0002_estudiante_programaeducativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='materias',
            field=models.ManyToManyField(related_name='estudiantesMaterias', to='materias.Materia'),
        ),
    ]
