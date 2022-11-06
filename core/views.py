from django.shortcuts import render
from.models import Produto

def index(request):

    produtos = Produto.objects.all()

    print(f" Headers {request.user}")
    context = {
        'curso': 'Progamação com Django',
        'outro': 'jango e massa',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    contac_itens = {
        'pessoas': 'cliente'
    }
    return render(request, 'contato.html', contac_itens)


def pedido(request):
    return render(request, 'pedido.html')
