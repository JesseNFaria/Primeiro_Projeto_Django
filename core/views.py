from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    Usuario = ''
    if str(request.user) != 'AnonymousUser':
      Usuario = f'Bem Vindo {request.user} !'

    if request.user.is_superuser:
        Adm = 'Sim'
    else:
        Adm = 'Não'

    context = {
       'usuario': Usuario,
       'sysadmin': Adm,
       'produtos' : produtos 
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, chave):
    prod = Produto.objects.get(id=chave)
    context = {
       'produto' : prod 
    }
    return render(request, 'produto.html', context)
