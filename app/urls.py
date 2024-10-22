from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name ='index'),
    path("<int:livro_id>/", views.detail, name="detail"),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('adicionar-livro/', views.adicionar_livro, name='adicionar_livro'),
    path('editar-livro/<int:livro_id>', views.editar_livro, name='editar_livro'),
    path('deletar_livro/<int:livro_id>/', views.deletar_livro, name='deletar_livro'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)