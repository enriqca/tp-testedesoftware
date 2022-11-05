from django.test import TestCase
from .models import Usuario
from .views import UsuarioView

# Create your tests here.

class CriarUsuario(TestCase):

  def test_criar_novo_usuario(self):
    pass

  def test_numero_usuarios(self):
    pass

  def test_criar_usuario_ja_existente(self):
    pass

class AlterarUsuario(TestCase):
  def test_alterar_nome_usuario(self):
    pass

  def test_alterar_nome_usuario_ja_existente(self):
    pass

  def test_alterar_senha(self):
    pass