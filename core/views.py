from django.shortcuts import render


def index(request):
    context = {
        'curso':'Progamação com Django',
        'outro':'jango e massa'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')