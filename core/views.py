from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import upper
from .models import Jogo
from .forms import JogoForm
from django.db.models import Count
import random
import string

def gerar_codigo_midia_digital(tamanho=20):
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return f'{codigo[:5]}-{codigo[5:10]}-{codigo[10:15]}-{codigo[15:]}'

def index(request):
    search_query = request.GET.get('search', '')
    tema = request.GET.get('tema', '')


    if search_query:
        jogos = Jogo.objects.filter(nome__icontains=search_query)
    elif tema:
        jogos = Jogo.objects.filter(tema=tema)
    else:
        jogos = Jogo.objects.all()

    count_jogos_no_carrinho = Jogo.objects.filter(no_carrinho=True).count()
    return render(request, 'index.html', {'jogos': jogos, 'search_query': search_query, 'tema': tema, 'count_jogos_no_carrinho': count_jogos_no_carrinho})


def adicionar_carrinho(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)

    if request.method == 'POST':
        jogo.no_carrinho = True
        jogo.save()

    return redirect('index')

def revisar_carrinho(request):
    jogos_no_carrinho = Jogo.objects.filter(no_carrinho=True)

    if request.method == 'POST':
        compras = []
        for jogo in jogos_no_carrinho:
            midia_fisica = request.POST.get(f'midia_fisica_{jogo.id}')
            midia_digital = request.POST.get(f'midia_digital_{jogo.id}')

            if midia_fisica or midia_digital:
                compra = {'jogo': jogo.nome, 'midia': ''}
                if midia_fisica:
                    compra['midia'] = 'Mídia Física (Será entregue em casa)'
                else:
                    # Gerar um código fictício para a mídia digital
                    codigo_midia_digital = upper( gerar_codigo_midia_digital())
                    compra['midia'] = f'Mídia Digital (Código: {codigo_midia_digital})'
                    jogo.codigo_midia_digital = codigo_midia_digital
                jogo.no_carrinho = False
                jogo.save()
                compras.append(compra)

        return render(request, 'compra_sucesso.html', {'compras': compras})

    return render(request, 'revisar_carrinho.html', {'jogos_no_carrinho': jogos_no_carrinho})

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



def funcionario(request):
    return render(request, 'area_func.html')