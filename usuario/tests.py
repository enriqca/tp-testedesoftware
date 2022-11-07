from django.test import TestCase
from .models import Usuario
from .views import UsuarioView

# Create your tests here.

class CriarUsuario(TestCase):

  def test_criar_novo_usuario(self):
    self.assertEqual(Usuario.objects.count(),0)
    usuario = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario.save()
    self.assertEqual(Usuario.objects.count(),1)

  def test_numero_usuarios(self):
    self.assertEqual(Usuario.objects.count(),0)
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    usuario2 = Usuario(usuario='marcialima',nome='Marcia Lima',email='marcia@lima',data_nascimento='2002-04-07', senha='123')
    usuario2.save()
    self.assertEqual(Usuario.objects.count(),2)

  def test_criar_usuario_ja_existente(self):
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    usuario2 = Usuario(usuario='marcialima',nome='Marcia Lima',email='marcia@lima',data_nascimento='2002-04-07', senha='123')
    usuario2.save()
    usuario3 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@a',data_nascimento='2002-04-07',senha='123')
    with self.assertRaises(Exception) as exception:
      usuario3.save()

  def test_criar_usuario_email_ja_utilizado(self):
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    usuario2 = Usuario(usuario='marcialima',nome='Marcia Lima',email='marcia@lima',data_nascimento='2002-04-07', senha='123')
    usuario2.save()
    usuario3 = Usuario(usuario='joaoa',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    with self.assertRaises(Exception) as exception:
      usuario3.save()

class AlterarUsuario(TestCase):
  def test_alterar_usuario(self):
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    user = Usuario.objects.get(usuario='joaosouza')
    self.assertEqual(user.usuario,'joaosouza')
    user.alterar_usuario('joaosouza','joaosousa')
    self.assertEqual(user.usuario,'joaosousa')

  def test_alterar_nome_usuario(self):
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    usuario1.alterar_nome('Joao Sousa')
    self.assertEqual(usuario1.nome,'Joao Sousa')
    

  def test_alterar_senha(self):
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    user = Usuario.objects.get(usuario='joaosouza')
    resultado = user.alterar_senha(user.usuario,user.senha)
    self.assertTrue(resultado)

class FazerLogin(TestCase):

    def test_fazer_login_usuario_existente(self):
      usuario = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
      usuario.save()
      resultado = UsuarioView.logar_usuario('joao@souza','123')
      self.assertTrue(resultado)

    def test_fazer_login_usuario_nao_existente(self):
      usuario = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
      usuario.save()
      with self.assertRaises(Exception) as exception:
        UsuarioView.logar_usuario('joao@a','123')

    def test_informar_senha_errada(self):
      usuario = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
      usuario.save()
      with self.assertRaises(Exception) as exception:
        UsuarioView.logar_usuario('joao@souza','12345')