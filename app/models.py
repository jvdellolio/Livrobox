from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django import forms

class Livro(models.Model):
    genero = models.CharField(max_length=50, default= '')
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    nota = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], null=True
    )
    imagem = models.ImageField(upload_to='livros/', default='livros/default.jpg')
    descrição = models.CharField (max_length= 1000, default= '')
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

def __str__(self):
    return self.titulo