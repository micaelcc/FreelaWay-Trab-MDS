from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/jobs/encontrar_jobs')
        else:
            return render(request, 'login.html')
    
    elif request.method == 'POST':
        user = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=user, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha inválidos')
            return redirect('/auth/login')
        
        else:
            auth.login(request, usuario)
            return redirect('/jobs/encontrar_jobs')


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/plataforma')
        else:
            return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if len(username.strip()) < 3:
            messages.add_message(request, constants.WARNING, 'Nome de usuário deve ter no mínimo 3 letras')
            return render(request,'cadastro.html')

        elif not senha == confirmar_senha:
            messages.add_message(request, constants.WARNING, 'As senhas digitadas não são iguais')
            return render(request,'cadastro.html')
        
        elif len(senha.strip()) < 4:
            messages.add_message(request, constants.WARNING, 'A Senha deve ter no mínimo 4 caracteres')
            return render(request, 'cadastro.html')
        
        # verifica se o usuario já existe no banco de dados
        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.WARNING, 'Este usuário já existe no sistema')
            return render(request,'cadastro.html')
        
        # cadastra o usuário no banco
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return redirect('/auth/cadastro')

        except:
            messages.add_message(request, constants.ERROR, 'Erro ao criar o usuário')
            return redirect('/auth/cadastro')

    return render('/auth/cadastro')


def sair(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/auth/login')

