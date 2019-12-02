# Generated by Django 2.2.7 on 2019-12-02 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maestros', '0001_initial'),
        ('grupos', '0007_remove_grupo_maestroasignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='maestroAsignado',
            field=models.ForeignKey(help_text='Seleccione un Maestro', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gruposMaestro', to='maestros.Maestro'),
        ),
    ]
