from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse

def login_view(request):
    """View personalizada para login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'login_simple.html')

def test_login(request):
    """View de teste para verificar se o sistema está funcionando"""
    return HttpResponse("<h1>Sistema funcionando!</h1><p>Login está OK</p>")
