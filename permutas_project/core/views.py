from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('login')

def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'core/dashboard.html')