from django.shortcuts import render
from despesas.models import Despesas

class DespesasView():
  def criar_despesa(despesa):
    return(despesa.nome)