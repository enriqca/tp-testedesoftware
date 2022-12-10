from django.shortcuts import render
from despesas.models import Despesas

def criar_despesa(request):
  return render(request, 'adicionar_despesa.html')

def add_despesa(request):
  nome_despesa = request.POST['nome_despesa']
  descricao_despesa = request.POST['descricao_despesa']
  valor_total_despesa = request.POST['valor_total_despesa']
  data_despesa = request.POST['data_despesa']
  tipo_divisao_desp = request.POST['tipo_divisao_desp']
  # nova_despesa = Despesas(nome=nome_despesa,descricao=descricao_despesa,data=data_despesa,tipo_divisao=tipo_divisao_desp,valor_total=valor_total_despesa)
  # nova_despesa = Despesas.objects.create(nome=nome_despesa)
  # print(nova_despesa)
  # nova_despesa.save()
  return render(request,'dashboard.html')