from django.test import TestCase
from .models import Despesas, SaldoDespesas
from django.contrib.auth.models import User

# Create your tests here.
class DespesasTest(TestCase):
  '''
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
  def test_remover_despesa(self):
    pass
  '''

  def test_ver_saldo_atual_com_determinado_usuario(self):    
    despesa1 = Despesas(valor_total = 10.00, valor_atribuido = [5.0, 5.0], tipo_divisao='IGUAL')
    despesa2 = Despesas(valor_total = 15.00, valor_atribuido = [5.0, 10.0], tipo_divisao='DESIGUAL')
    despesa3 = Despesas(valor_total = 10.00, valor_atribuido = [0.1, 0.9], tipo_divisao='PERCENTUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa1, despesa2, despesa3])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa1, despesa2, despesa3])
    self.assertEqual(saldo_user1, 24.00)
    self.assertEqual(saldo_user2, -24.00)

  def test_editar_valor_cobrado_na_despesa(self):
    despesa = Despesas(valor_total = 15.00, valor_atribuido = [5.0, 10.0], tipo_divisao='DESIGUAL')
    nova_despesa = Despesas(valor_total = 25.00, valor_atribuido = [5.0, 20.0], tipo_divisao='DESIGUAL')
    despesa.editar_despesa(nova_despesa)
    self.assertEqual(despesa.valor_total, 25.00)

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

  def test_valida_valores_atribuidos_igualmente(self):
    despesas = Despesas()
    total = 15.00
    valores1 = [7.6, 7.5]
    valores2 = [7.5, 7.50]

    self.assertFalse(despesas.valida_valores_atribuidos(total, valores1, 'DESIGUAL'))
    self.assertTrue(despesas.valida_valores_atribuidos(total, valores2, 'DESIGUAL'))

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
    user1 = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    user2 = User(username='marciamo',email='marcia@moreira',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Moreira')

    despesa = Despesas(valor_total = 15.00, valor_atribuido = [10.00, 5.00], tipo_divisao='DESIGUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa])
    self.assertEqual(saldo_user1, 5.00)
    self.assertEqual(saldo_user2, -5.00)

  def test_calculo_saldo_determinada_despesa_igual(self):
    user1 = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    user2 = User(username='marciamo',email='marcia@moreira',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Moreira')

    despesa = Despesas(valor_total = 10.00, valor_atribuido = [5.00, 5.00], tipo_divisao='IGUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa])
    self.assertEqual(saldo_user1, 5.00)
    self.assertEqual(saldo_user2, -5.00)

  def test_calculo_saldo_determinada_despesa_percentual(self):
    despesa = Despesas(valor_total = 10.00, valor_atribuido = [0.1, 0.9], tipo_divisao='PERCENTUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa])
    self.assertEqual(saldo_user1, 9.00)
    self.assertEqual(saldo_user2, -9.00)


  def test_calculo_saldo_mais_de_uma_despesa_com_determinado_usuario_percentual(self):
    despesa1 = Despesas(valor_total = 10.00, valor_atribuido = [0.1, 0.9], tipo_divisao='PERCENTUAL')
    despesa2 = Despesas(valor_total = 10.00, valor_atribuido = [0.1, 0.9], tipo_divisao='PERCENTUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa1, despesa2])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa1, despesa2])
    self.assertEqual(saldo_user1, 18.00)
    self.assertEqual(saldo_user2, -18.00)
  
  def test_calculo_saldo_mais_de_uma_despesa_com_determinado_usuario_igual(self):
    despesa1 = Despesas(valor_total = 10.00, valor_atribuido = [5.0, 5.0], tipo_divisao='IGUAL')
    despesa2 = Despesas(valor_total = 15.00, valor_atribuido = [5.0, 10.0], tipo_divisao='IGUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa1, despesa2])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa1, despesa2])
    self.assertEqual(saldo_user1, 15.00)
    self.assertEqual(saldo_user2, -15.00)
  
  def test_calculo_saldo_mais_de_uma_despesa_com_determinado_usuario_desigual(self):
    despesa1 = Despesas(valor_total = 15.00, valor_atribuido = [5.0, 10.0], tipo_divisao='DESIGUAL')
    despesa2 = Despesas(valor_total = 10.00, valor_atribuido = [10.0, 5.0], tipo_divisao='DESIGUAL')
    saldos = SaldoDespesas()
    saldo_user1 = saldos.calcula_saldo_usuario('user1', ['user1','user2'], [despesa1, despesa2])
    saldo_user2 = saldos.calcula_saldo_usuario('user2', ['user1','user2'], [despesa1, despesa2])
    self.assertEqual(saldo_user1, 15.00)
    self.assertEqual(saldo_user2, -15.00)

'''
  def test_calculo_total_todas_despesas(self):
    pass
'''
