#imports necessarios.
import re

from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta

#funcao da tela login_user
def login_user(request):
    return render(request, 'login.html')

#funcao do botao
def logout_user(request):
    logout(request)
    return redirect('/')

#funcao do botao submit
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:#mensagem de erro ao logar.
            messages.error(request,"Usuario ou senha invalido")
    return redirect('/')

@login_required(login_url='/login/')#direcionando para a tela de login.

#funcao de eventos do html da pagina agenda.
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario, data_evento__lt=data_atual)
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)

#funcao evento para insercao
@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)

    return render(request, 'evento.html',dados)#direciona para o html da pagina evento.

#informações da classe Evento.
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,data_evento=data_evento,
                                  descricao=descricao,usuario=usuario)
        # Evento.objects.create(titulo=titulo,data_evento=data_evento,
        #                       descricao=descricao,usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()

    return redirect('/')







