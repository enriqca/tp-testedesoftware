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
  def test_alterar_nome_usuario(self):
    usuario1 = Usuario(usuario='joaosouza',nome='Joao Souza',email='joao@souza',data_nascimento='2002-04-07',senha='123')
    usuario1.save()
    user = Usuario.objects.get(usuario='joaosouza')
    self.assertEqual(user.nome,'Joao Souza')
    user.alterar_usuario('Joao Sousa', 'joaosouza')
    self.assertEqual(user.nome,'Joao Sousa')

  def test_alterar_nome_usuario_ja_existente(self):
    pass

  def test_alterar_senha(self):
    pass