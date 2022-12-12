from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('criar_despesa', criar_despesa, name='criar_despesa')
]