# Generated by Django 5.1.1 on 2024-09-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='genero',
            field=models.CharField(default='', max_length=50),
        ),
    ]
