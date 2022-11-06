from django.db import models

# Create your models here.

class Usuario(models.Model):
  usuario = models.CharField(max_length=40)
  nome = models.CharField(max_length=256)
  email = models.CharField(max_length=100)
  data_nascimento = models.DateField()

  def __str__(self) -> str:
    return self.usuario