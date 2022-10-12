from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader


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
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'prod': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')

    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)


def error500(request):
    template = loader.get_template('500.html')

    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)
