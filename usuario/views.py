from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from .models import Usuario
from django.views.decorators.http import require_POST
from main.templates import *

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
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])
        usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["password"])
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/dashboard')
    except User.DoesNotExist:
        error = "Usuário não cadastrado"

    return render(request, 'login.html', {'error': error})

def logout(request):
    django_logout(request)
    return redirect('/')
