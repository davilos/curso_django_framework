from django.shortcuts import render


def index(request):
    print(dir(request))
    print(dir(request.user))

    if request.user.is_anonymous:
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado': teste
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.user.is_staff:
        return render(request, 'contact.html')
    return render(request, 'permissions.html')
