from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.SET_NULL, null=True,  blank=True, related_name='veiculos')  
    cor = models.ForeignKey('Cor', on_delete=models.SET_NULL, null=True, blank=True, related_name='veiculos')
    acessorios = models.ManyToManyField('Acessorio', related_name='veiculos')


    def __str__(self):
        return f'{self.id} - {self.modelo} {self.cor} ({self.ano})'