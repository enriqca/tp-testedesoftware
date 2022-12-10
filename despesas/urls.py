from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('adicionar_despesa', criar_despesa, name='adicionar_despesa'),
    path('add_despesa', add_despesa, name='add_despesa')
]