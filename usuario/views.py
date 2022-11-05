from django.shortcuts import redirect, render
from usuario.models import Usuario

class UsuarioView():
  def criar_usuario(usuario):
    return(usuario.nome)