# Generated by Django 5.1.1 on 2024-09-18 19:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_livro_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='nota',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
