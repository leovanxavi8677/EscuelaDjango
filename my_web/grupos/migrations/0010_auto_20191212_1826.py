# Generated by Django 2.2.7 on 2019-12-12 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0009_auto_20191211_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='numeroAlumnos',
            field=models.CharField(max_length=2, validators=[django.core.validators.validate_integer]),
        ),
    ]
