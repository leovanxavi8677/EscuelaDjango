# Generated by Django 2.2.7 on 2019-11-21 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0002_grupo_maestroasignado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='maestroAsignado',
        ),
    ]