from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('cadastrar', cadastrar_usuario, name='cadastrar'),
    path('logar', logar_usuario, name='logar'),
    path('logout', logout, name='logout'),
]