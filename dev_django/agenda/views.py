from django.shortcuts import render, HttpResponse, redirect
from agenda.models import Evento
from django.contrib.auth.decorators import login_required # Realizando isso ele só irá abrir a minha página se eu estiver logado.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def evento(request):
    id_event = request.GET.get("id")
    data = {}
    if id_event:
        data['evento'] = Evento.objects.get(id = id_event)
    return render(request, 'evento.html', data)


def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def submit_evento(request): # Feature for increment data in database.
    if request.POST:
        title = request.POST.get('title')
        datetime = request.POST.get('datetime')
        description = request.POST.get('description')
        local = request.POST.get('address')
        user = request.user
        id_event = request.POST.get('id') # Esse Id eu só pego para poder fazer a edição.
        if id_event:
            Evento.objects.filter(id=id_event).update(titulo = title, descricao = description, data_evento = datetime, local=local)
        else:
            Evento.objects.create(titulo = title, descricao = description, data_evento = datetime, usuario = user, local=local)
    return redirect("/agenda/") # redirect to home.


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    user = request.user
    event = Evento.objects.get(id=id_evento)
    if user == event.usuario: # Valida se aquele evento é daquele usuário, se não for ele não exclui.
        event.delete() # Id receive and event delete.
    return redirect('/agenda/')


def submit_login(request): # Feature Login
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # authenticate user
        if user is not None:
            login(request, user)
            return redirect("/agenda/")
        else:
            messages.error(request, "Usuário ou senha inválido!")
    return redirect('login')


# Log out of the page
def logout_user(request):
    logout(request)
    return redirect('login')

    
@login_required(login_url='/login/') # Coloco isso pra identificar que as funções abaixo são decoradores.
def home(request):
    user = request.user
    #data_atual = datetime.now() # Pega o horário atual
    event = Evento.objects.filter(usuario=user) # Cath all the files into my class Evento # __gt se refere á um valor maior __lt para um valor menor. # Fazendo essa query ele só irá me trazer os eventos futuros e não mais os que venceram.
    data = {'eventos': event}
    return render(request, "agenda.html", data)