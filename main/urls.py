from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
  path('', home_page, name='home'),
  path('login', login_page, name='login'),
  path('dashboard', dashboard_page, name='dashboard'),
  path('cadastro', cadastro_page, name='cadastro'),
  path('historico', historico_page, name='historico'),
  path('graficos', graficos_page, name='graficos'),
  path('adicionardespesa', adicionar_despesa_page, name='adicionardespesa'),
  path('quitardividas', quitar_dividas_page, name='quitardividas'),
]