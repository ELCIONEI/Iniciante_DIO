from django.shortcuts import render

# Create your views here.

def login_usuario (request):
    return render(request,'LoginUsuario.html')

def cadastro_usuarios(request):
    return render(request, 'CadastroUsuarios.html')

def chamados(request):
    return render(request,'Chamados.html')