# Generated by Django 2.2.7 on 2019-11-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]
