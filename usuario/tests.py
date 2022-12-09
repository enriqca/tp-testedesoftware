from django.test import TestCase, Client
from .views import *
from django.contrib.auth.models import User

# Create your tests here.

class TestCriarUsuario(TestCase):

  def test_criar_novo_usuario(self):
    self.assertEqual(User.objects.count(),0)
    usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    usuario.save()
    self.assertEqual(User.objects.count(),1)

  def test_numero_usuarios(self):
    self.assertEqual(User.objects.count(),0)
    usuario1 = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    usuario1.save()
    usuario2 = User(username='marciamo',email='marcia@moreira',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Moreira')
    usuario2.save()
    self.assertEqual(User.objects.count(),2)

class TestExcecaoCriarUsuario(TestCase):

  def setUp(self):
    usuario1 = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    usuario1.save()
    usuario2 = User(username='marciamo',email='marcia@moreira',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Moreira')
    usuario2.save()

  def test_criar_usuario_ja_existente(self):
    usuario3 = User(username='marciamo',email='marcia@mold',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Mold')
    with self.assertRaises(Exception) as exception:
      usuario3.save()

  # def test_criar_usuario_email_ja_utilizado(self):
  #   usuario3 = User(username='henrique.alves',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Alves')
  #   with self.assertRaises(Exception) as exception:
      # usuario3.save()

# class AlterarUsuario(TestCase):
#   def test_alterar_usuario(self):
#     usuario1 = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
#     usuario1.save()
#     user = User.objects.get(email='rick@a')
#     self.assertEqual(user.username,'enriqca')
    # user.alterar_usuario('joaosouza','joaosousa')
    # self.assertEqual(user.usuario,'joaosousa')

#   def test_alterar_nome_usuario(self):
#     usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
#     usuario1.save()
#     usuario1.alterar_nome('Joao Sousa')
#     self.assertEqual(usuario1.nome,'Joao Sousa')
    

#   def test_alterar_senha(self):
#     usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
#     usuario1.save()
#     user = Usuario.objects.get(usuario='joaosouza')
#     resultado = user.alterar_senha(user.usuario,user.senha)
#     self.assertTrue(resultado)

class TestLogin(TestCase):

    def test_fazer_login_usuario_existente(self):
      usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
      usuario.save()
      response = self.client.post('/login',{'username': usuario.username, 'password': usuario.password})
      self.assertEqual(response.status_code,200)

    def test_fazer_login_usuario_nao_existente(self):
      usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
      usuario.save()
      response = self.client.post('/login',{'username': 'henrique@a', 'password': '123'})
      self.assertTemplateUsed(response,'login.html')

#     def test_informar_senha_errada(self):
#       usuario = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
#       usuario.save()
#       with self.assertRaises(Exception) as exception:
#         UsuarioView.logar_usuario('joao@souza','12345')