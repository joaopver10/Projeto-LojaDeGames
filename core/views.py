from django.shortcuts import render, get_object_or_404, redirect
from .models import Jogo
from .forms import JogoForm


def index(request):
    search_query = request.GET.get('search', '')
    tema = request.GET.get('tema', '')

    if search_query:
        jogos = Jogo.objects.filter(nome__icontains=search_query)
    elif tema:
        jogos = Jogo.objects.filter(tema=tema)
    else:
        jogos = Jogo.objects.all()

    return render(request, 'index.html', {'jogos': jogos, 'search_query': search_query, 'tema': tema})

def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'lista_jogos.html', {'jogos': jogos})

def detalhe_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    return render(request, 'detalhe_jogo.html', {'jogo': jogo})

def adicionar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            jogo = form.save(commit=False)
            jogo.imagem = request.FILES.get('imagem')
            jogo.save()
            return redirect('lista_jogos')
    else:
        form = JogoForm()
    return render(request, 'adicionar_jogo.html', {'form': form})

def editar_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES, instance=jogo)
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

def visualizar_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    return render(request, 'visualizar_jogo.html', {'jogo': jogo})