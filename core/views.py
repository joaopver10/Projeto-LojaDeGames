from django.shortcuts import render, get_object_or_404, redirect
from .models import Jogo
from .forms import JogoForm


def index(request):
    return render(request, 'index.html')

def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'lista_jogos.html', {'jogos': jogos})

def detalhe_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    return render(request, 'detalhe_jogo.html', {'jogo': jogo})

def adicionar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jogos')
    else:
        form = JogoForm()
    return render(request, 'adicionar_jogo.html', {'form': form})

def editar_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('lista_jogos')
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'editar_jogo.html', {'form': form, 'jogo': jogo})

def excluir_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    jogo.delete()
    return redirect('lista_jogos')
