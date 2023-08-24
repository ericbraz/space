from django.shortcuts import render, get_object_or_404
from galery.models import Fotografia


def index(request):
    data = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, "galery/index.html", {"cards": data})


def imagem(request, foto_id):
    data = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, "galery/imagem.html", {"fotografia": data})

def buscar(request):
    data = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            data = data.filter(nome__contains=nome_a_buscar)

    return render(request, 'galery/buscar.html', {"cards": data})
