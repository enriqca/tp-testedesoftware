from django.db import models

# Create your models here.

class Usuario(models.Model):
  usuario = models.CharField(max_length=40,unique=True)
  nome = models.CharField(max_length=256)
  email = models.CharField(max_length=100,unique=True)
  data_nascimento = models.DateField()
  senha = models.CharField(max_length=32, default=False)

  def __str__(self) -> str:
    return self.usuario

  def alterar_usuario(self,usuarioantigo,usuarionovo):
    if(usuarioantigo==self.usuario):
        self.usuario = usuarionovo
    else:
      raise Exception('Usuário não autorizado')

  def alterar_nome(self,nome):
    self.nome = nome

  def alterar_senha(self,usuario,senha):
    if(usuario==self.usuario):
      self.senha = senha
      return True
    else:
      raise Exception('Usuário não permitido')

  