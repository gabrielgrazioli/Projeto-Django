from django.shortcuts import render, redirect
from django.contrib.auth import logout

def inicio(request):
    return render(request, 'inicio.html')

def sobre(request):
    return render(request, 'sobre.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def logout_view(request):
    logout(request)
    return redirect('login')