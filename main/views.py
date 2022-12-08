from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from main.models import 

def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

@login_required(login_url='/logar')
def dashboard_page(request):
    return render(request, 'dashboard.html')

def cadastro_page(request):
    return render(request, 'cadastro.html')

def historico_page(request):
    return render(request, 'historico.html')

def graficos_page(request):
    return render(request, 'graficos.html')