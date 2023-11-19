from django import forms
from .models import Jogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'tema', 'descricao', 'sistema_avaliacao', 'imagem']

    sistema_avaliacao = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], widget=forms.Select(attrs={'class': 'form-control'}))
    imagem = forms.ImageField(widget=forms.ClearableFileInput(), required=False)
