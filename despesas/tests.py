from django.test import TestCase
from .models import Despesas, SaldoDespesas
from usuario.models import Usuario

# Create your tests here.
class DespesasTest(TestCase):
  def test_ver_historico_despesas(self):
    pass
  
  def test_ver_historico_com_determinado_usuario(self):
    pass
  def test_ver_saldo_geral_atual(self):
    pass
  def test_ver_saldo_atual_com_determinado_usuario(self):
    pass
  def test_criar_despesa_com_um_usuario(self):
    pass
  def test_criar_despesa_com_mais_de_um_usuario(self):
    pass
  def test_editar_valor_cobrado_na_despesa(self):
    pass
  def test_remover_despesa(self):
    pass

class CalculoDespesasTest(TestCase):
  def test_calculo_despesa_dividida_igualmente(self):
    despesas = Despesas()
    usuarios = ['user1', 'user2', 'user3']
    valor_total = 15.30
    divisao = despesas.calculo_divisao_igual(valor_total, usuarios)
    self.assertEqual(divisao, [5.10, 5.10, 5.10])

  def test_calculo_despesa_dividida_desigualmente(self):
    despesas = Despesas()
    usuarios = ['user1', 'user2', 'user3']
    valor_total = 15.00
    valores = [3.0, 7.0, 5.0]
    divisao = despesas.calculo_divisao_desigual(valor_total,valores, usuarios)
    self.assertEqual(divisao, [3.0, 7.0, 5.0])

  def test_calculo_despesa_dividida_percentualmente(self):
    despesas = Despesas()
    usuarios = ['user1', 'user2', 'user3']
    valor_total = 15.00
    valores = [0.1, 0.5, 0.4]
    divisao = despesas.calculo_divisao_percentual(valor_total,valores, usuarios )
    self.assertEqual(divisao, [1.50, 7.5, 6.0])

  def test_valida_valores_atribuidos_desigualmente(self):
    despesas = Despesas()
    total = 15.00
    valores1 = [5.0, 9.0]
    valores2 = [5.0, 10.00]

    self.assertFalse(despesas.valida_valores_atribuidos(total, valores1, 'DESIGUAL'))
    self.assertTrue(despesas.valida_valores_atribuidos(total, valores2, 'DESIGUAL'))

  def test_valida_valores_atribuidos_percentualmente(self):
    despesas = Despesas()
    total = 15.00
    valores1 = [0.1, 0.7]
    valores2 = [0.6, 0.4]

    self.assertFalse(despesas.valida_valores_atribuidos(total, valores1, 'PERCENTUAL'))
    self.assertTrue(despesas.valida_valores_atribuidos(total, valores2, 'PERCENTUAL'))

  def test_calculo_saldo_determinada_despesa_desigual(self):
    user1 = Usuario(nome='user1')
    user2 = Usuario(nome='user2')

    despesa = Despesas(valor_total = 10.00, valor_atribuido = [10.00, 5.00], tipo_divisao='DESIGUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa])
    self.assertEqual(saldo_user1, 5.00)
    self.assertEqual(saldo_user2, -5.00)

  def test_calculo_total_despesas_com_determinado_usuario(self):
    pass

  def test_calculo_total_todas_despesas(self):
    pass