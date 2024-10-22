from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Livro
from django.http import Http404
from app.forms import LoginForms, CadastroForms, LivroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    livros = Livro.objects.order_by("ano_publicacao")
    return render(request, 'app/index.html', {'livros': livros})

def detail(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    estrelas_inteiras = int(livro.nota)
    meia_estrela = livro.nota - estrelas_inteiras >= 0.5
    lista_estrelas_inteiras = range(estrelas_inteiras)
    return render (request, "app/detail.html", {
        "livro": livro, 
        'lista_estrelas_inteiras': lista_estrelas_inteiras,
        'meia_estrela': meia_estrela,
        'lista_5': [1,2,3,4,5]
    })

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome= form['nome_login'].value()
            senha= form['senha'].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        ) 
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request, f"{nome} Logado com sucesso!")
            return redirect ('index')
        else:
            messages.error(request, "Erro ao efetuar o login, tente de novo")
            return redirect('login')


    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
         
            
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,"Usuário já existe, tente de novo")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')

def adicionar_livro(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    form = LivroForms
    if request.method == "POST":
        form = LivroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo livro adicionado!')
            return redirect('index')
        else:
            print(form.errors)

    return render(request, 'app/adicionar_livro.html', {'form': form})

def editar_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    form = LivroForms(instance=livro)

    if request.method == 'POST':
        form = LivroForms(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro editado!')
            return redirect('index')

    return render(request, 'app/editar_livro.html', {'form': form, 'livro_id': livro_id})

def deletar_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    livro.delete()
    messages.success(request, 'Livro deletado!')
    return redirect('index')
