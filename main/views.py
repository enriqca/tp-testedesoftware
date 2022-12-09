from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# from main.models import 

def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    else:
        return render(request, 'login.html')

def dashboard_page(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect('/login')

def cadastro_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    else:
        return render(request, 'cadastro.html')

def historico_page(request):
    return render(request, 'historico.html')

def graficos_page(request):
    return render(request, 'graficos.html')