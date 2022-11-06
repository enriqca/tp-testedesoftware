from django.db import models
from django.contrib.postgres.fields import ArrayField
from usuario.models import Usuario

# Create your models here.
class Despesas(models.Model):
  nome = models.CharField(max_length=256)
  descricao = models.CharField(max_length=256)
  data = models.CharField(max_length=256)
  usuario_criador =  models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, default=None, related_name='criador')
  usuarios_relacionados = models.ManyToManyField(Usuario, related_name='relacionados') #o primeiro usuario será sempre o que pagou
  status = models.BooleanField(default=True)

  DIV_IGUAL = 'IGUAL'
  DIV_DESIG = 'DESIGUAL'
  DIV_PERCE = 'PERCENTUAL'
  DIVISAO_CHOICES = [
      (DIV_IGUAL, 'Dividido igualmente'),
      (DIV_DESIG, 'Dividido desigualmente'),
      (DIV_PERCE, 'Dividido percentualmente'),
  ]

  tipo_divisao = models.CharField(
      max_length=25,
      choices=DIVISAO_CHOICES,
      default=DIV_IGUAL,
  )

  valor_total = models.FloatField()
  valor_atribuido = ArrayField(models.FloatField()) #valor atribuido a cada usuario de acordo com a divisão

  def __str__(self) -> str:
    return self.nome

  def editar_despesa(self, NovaDespesa):
    self.nome = NovaDespesa.nome
    self.descricao = NovaDespesa.descricao
    self.data = NovaDespesa.data
    self.usuario_criador = NovaDespesa.usuario_criador
    self.usuarios_relacionados = NovaDespesa.usuarios_relacionados
    self.tipo_divisao = NovaDespesa.tipo_divisao
    self.valor_total = NovaDespesa.valor_total
    self.valor_atribuido = NovaDespesa.valor_atribuido

  def valida_valores_atribuidos(self, valor_total, valor_atribuido, tipo_divisao):
    total = sum(valor_atribuido)
    if(tipo_divisao == 'DESIGUAL'):
      return total == valor_total
    if(tipo_divisao == 'PERCENTUAL'):
      return total == 1

  #Retorna na mesma ordem dos usuarios relacionados o total a ser pago por cada.
  def calculo_divisao_igual(self, valor_total, usuarios_relacionados):
    valor_dividido = []
    div = round(valor_total/len(usuarios_relacionados), 2)
    for u in usuarios_relacionados:
      valor_dividido.append(div)
    return valor_dividido

  def calculo_divisao_desigual(self, valor_total, valor_atribuido, usuarios_relacionados):
    valor_dividido = []
    valor_restante = valor_total
    for i in range(len(usuarios_relacionados)):
      valor_restante = valor_restante - valor_atribuido[i]
      valor_dividido.append(valor_atribuido[i])
    return valor_dividido

  def calculo_divisao_percentual(self, valor_total, valor_atribuido, usuarios_relacionados):
    valor_dividido = []
    for i in range(len(usuarios_relacionados)):
      valor_percentual = round(valor_total * valor_atribuido[i], 2)
      valor_dividido.append(valor_percentual)
    return valor_dividido

class SaldoDespesas(models.Model):
  #despesas = ArrayField(models.ForeignKey(Despesas, on_delete=models.DO_NOTHING, default=None))
  despesas = models.ManyToManyField(Despesas)

  def calcula_saldo_usuario(self, usuario, usuarios_relacionados, lista_despesas):
    saldo = 0
    for despesa in lista_despesas:
      if despesa.status == True:
        index = usuarios_relacionados.index(usuario)
        valores = despesa.valor_atribuido
        if(index == 0): #usuario que pagou, então os outros devem ele
          valores.pop(0) 
          if(despesa.tipo_divisao == 'IGUAL' or despesa.tipo_divisao == 'DESIGUAL'):
            saldo = saldo + sum(valores)
          else: #divisão percentual
            saldo = saldo + sum(valores)*despesa.valor_total
        else: #usuario que deve outro usuario
          if(despesa.tipo_divisao == 'IGUAL' or despesa.tipo_divisao == 'DESIGUAL'):
            saldo = saldo - valores[index-1]
          else:
            saldo = saldo - valores[index-1]*despesa.valor_total
    return saldo
        

