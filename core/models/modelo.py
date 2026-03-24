from django.db import models

class Modelo(models.Model):
    nome = models.CharField()
    marca = models.CharField(max_length=80, null=True, blank=True)
    categoria = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.nome}'
