from django.shortcuts import render, redirect
# from main.models import 

def home_page(request):
    return render(request, 'index.html')