from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns=[
  path('', home_page, name='home'),
  path('login', login_page, name='login'),
  path('dashboard', dashboard_page, name='dashboard'),
  path('cadastro', cadastro_page, name='cadastro'),
  path('dashboard/historico', historico_page, name='historico'),
  path('dashboard/graficos', graficos_page, name='graficos'),
]