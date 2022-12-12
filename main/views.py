from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from despesas.models import Despesas


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
    query = Despesas.objects.all()
    context = {
        'despesas': query
    }
    return render(request, 'historico.html', context=context)

def graficos_page(request):
    return render(request, 'graficos.html')

def adicionar_despesa_page(request):
    if request.method == 'GET':
        return render(request, 'adicionardespesa.html')
    else:
        nome_despesa = request.POST['nome_despesa']
        descricao_despesa = request.POST['descricao_despesa']
        valor_total_despesa = request.POST['valor_total_despesa']
        data_despesa = request.POST['data_despesa']
        tipo_divisao_desp = request.POST['tipo_divisao_desp']
        valores_atribuidos = request.POST['valor_atribuido']#.split(';')
        nova_despesa = Despesas(nome=nome_despesa,descricao=descricao_despesa,data=data_despesa,tipo_divisao=tipo_divisao_desp,valor_total=valor_total_despesa, valor_atribuido=valores_atribuidos)
        nova_despesa.save()
            
        context = {
            'resposta': 'Despesa criada com sucesso!' 
        }
        return render(request, 'adicionardespesa.html', context=context)


def quitar_dividas_page(request):
    return render(request, 'quitardividas.html')