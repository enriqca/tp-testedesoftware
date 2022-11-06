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

  def alterar_usuario(self,nome,usuario):
    self.usuario = usuario
    self.nome = nome

  # def alterar_senha(self,dados_usuario):
  #   self.senha = dados_usuario.senha

  