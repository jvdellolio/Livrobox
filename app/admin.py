from django.contrib import admin
from .models import Livro

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "autor", "titulo", "descrição", "ano_publicacao")
    list_display_links = ("id", "titulo")  # Removi "autor" dos links
    search_fields = ("autor", "titulo")
    list_filter = ("genero", "usuario")
    list_editable = ("ano_publicacao",)  # Ano de publicação pode ser editável agora
    list_per_page = 10

admin.site.register(Livro, ListandoLivros)