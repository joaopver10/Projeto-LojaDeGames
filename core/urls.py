from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import index, lista_jogos, detalhe_jogo, adicionar_jogo, editar_jogo, excluir_jogo


urlpatterns = [
    path('', index),
    path('jogos/', lista_jogos, name='lista_jogos'),
    path('jogos/<int:jogo_id>/', detalhe_jogo, name='detalhe_jogo'),
    path('jogos/adicionar/', adicionar_jogo, name='adicionar_jogo'),
    path('jogos/editar/<int:jogo_id>/', editar_jogo, name='editar_jogo'),
    path('jogos/excluir/<int:jogo_id>/', excluir_jogo, name='excluir_jogo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

