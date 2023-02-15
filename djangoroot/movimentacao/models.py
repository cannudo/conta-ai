from django.db import models

# Create your models here.
class Movimentacao(models.Model):
    titulo = models.CharField(max_length = 35)
    descricao = models.TextField(max_length = 70, null = True)
    entrada = models.BooleanField(default = True)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return f'R$ {self.valor} — {self.titulo} [{self.data.day}/{self.data.month}/{self.data.year}]'