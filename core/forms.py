from django import forms
from .models import Jogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'tema', 'descricao', 'sistema_avaliacao']