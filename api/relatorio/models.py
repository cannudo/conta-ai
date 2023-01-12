from django.db import models


# Create your models here.
class Relatorio(models.Model):
     descricao = models.CharField(max_length = 35)
     data = models.DateField()
     movimentacoes = models.ManyToManyField('movimentacao.Movimentacao')