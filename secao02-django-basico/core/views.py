from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.user.is_staff:
        return render(request, 'contact.html')
    return render(request, 'permissions.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'prod': prod
    }
    return render(request, 'produto.html', context)
