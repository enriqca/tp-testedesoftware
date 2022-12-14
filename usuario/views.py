from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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

    return render(request, 'login.html')

def logout(request):
    django_logout(request)
    return redirect('/')

def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})