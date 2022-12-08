from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usuario
from django.views.decorators.http import require_POST
from main.templates import *
# Create your views here.

@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return render(request, 'cadastro.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
        try:
            usuario_aux = User.objects.get(email=request.POST['username'])

            if usuario_aux:
                return render(request, 'cadastro.html', {'msg': 'Erro! Já existe um usuário com o mesmo username'})
        
        except User.DoesNotExist:
            nome_usuario = request.POST['username']
            primeiro_nome = request.POST['firstName']
            segundo_nome = request.POST['lastName']
            email = request.POST['email']
            senha = request.POST['password']

            novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha, first_name=primeiro_nome, last_name=segundo_nome)
            novoUsuario.save()
    return render(request,'login.html')

@require_POST
def logar_usuario(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["password"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/dashboard')

    return HttpResponseRedirect('/dashboard')

# def cadastrar_usuario(request):
#     if request.method == "POST":
#         form_usuario = UserCreationForm(request.POST)
#         if form_usuario.is_valid():
#             form_usuario.save()
#             return redirect('/dashboard')
#     else:
#         form_usuario = UserCreationForm()
#     return render(request, 'cadastro.html', {'form_usuario': form_usuario})

# def logar_usuario(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         usuario = authenticate(request, username=username, password=password)
#         if usuario is not None:
#             login(request, usuario)
#             return redirect('index')
#         else:
#             form_login = AuthenticationForm()
#     else:
#         form_login = AuthenticationForm()
#     return render(request, 'login.html', {'form_login': form_login})

# class UsuarioView():
#   def criar_usuario(usuario):
#     return(usuario.nome)

#   def logar_usuario(email_usuario,senha_usuario):
#     usuario_login = Usuario.objects.get(email=email_usuario)
#     if(usuario_login):
#         if(usuario_login.senha == senha_usuario):
#             return True
#         else:
#             raise Exception('Senha incorreta')
#     else:
#         raise Exception('Email não cadastrado')
