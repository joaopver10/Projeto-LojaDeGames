from django.db import models

class Jogo(models.Model):
    tema_choices = [
        ('ação', 'Ação'),
        ('terror', 'Terror'),
        ('rpg', 'RPG'),
        ('sobrevivência', 'Sobrevivência'),
        ('enigma', 'Enigma'),
        ('corrida', 'Corrida'),
    ]

    nome = models.CharField(max_length=100)
    tema = models.CharField(max_length=20, choices=tema_choices)
    descricao = models.TextField()
    sistema_avaliacao = models.DecimalField(max_digits=3, decimal_places=2)
    imagem = models.ImageField(upload_to='jogos', null=True, blank=True)
