from django.shortcuts import render

def index(request):
    print(request.user)
    print(str(request.user) != 'AnonymousUser')
    Usuario = ''
    if str(request.user) != 'AnonymousUser':
      Usuario = f'Bem Vindo {request.user} !'

    if request.user.is_superuser:
        Adm = 'Sim'
    else:
        Adm = 'Não'

    context = {
       'usuario': Usuario,
       'sysadmin': Adm
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')