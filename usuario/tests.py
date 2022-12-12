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

  def test_criar_usuario_ja_existente(self):
    usuario1 = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    usuario1.save()
    usuario2 = User(username='marciamo',email='marcia@moreira',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Moreira')
    usuario2.save()
    usuario3 = User(username='marciamo',email='marcia@mold',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Marcia', last_name='Mold')
    with self.assertRaises(Exception) as exception:
      usuario3.save()

  def test_view_cadastro_usuario(self):
    usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
    usuario.save()
    response = self.client.post('/cadastrar',{'email': usuario.email, 'password': usuario.password, 'username': usuario.username, 'firstName': usuario.first_name, 'lastName': usuario.last_name})
    self.assertEqual(response.status_code,200)

class TestAlterarUsuario(TestCase):
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
    
    def test_alterar_senha(self):
      usuario = User(username='enriqca',email='rick@a',password='henrique20',first_name='Henrique', last_name='Souza')
      usuario.save()
      response_login = self.client.post('/login',{'username': 'rick@a', 'password': 'henrique20'})
      self.assertEqual(response_login.status_code,200)
      response = self.client.post('/alterar_senha',{'request.user':usuario, 'request.POST.old_password': usuario.password, 'request.POST.new_password1': 'henrique10', 'request.POST.new_password2': 'henrique10'})
      self.assertEqual(response.status_code,200)

class TestLogin(TestCase):

    def test_view_fazer_login_usuario_existente(self):
      usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
      usuario.save()
      response = self.client.post('/logar',{'email': usuario.email, 'password': usuario.password})
      self.assertEqual(response.status_code,200)

    def test_view_fazer_login_usuario_nao_existente(self):
      usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
      usuario.save()
      response = self.client.post('/logar',{'email': 'henrique@a', 'password': '123'})
      self.assertTemplateUsed(response,'login.html')

    def test_logout(self):
      usuario = User(username='enriqca',email='rick@a',password='pbkdf2_sha256$390000$t0uqkHvtM0GFojVbIQBEnW$cqcpLwGVogOmz4GKF6+xf8BDaTsnq93/b37RooUuhjE=',first_name='Henrique', last_name='Souza')
      usuario.save()
      response_login = self.client.post('/logar',{'email': usuario.email, 'password': usuario.password})
      self.assertEqual(response_login.status_code,200)
      response_logout = self.client.post('/logout')
      self.assertRedirects(response_logout, '/')