# Generated by Django 2.2.7 on 2019-12-11 13:51

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_auto_20191210_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='passwd',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]
