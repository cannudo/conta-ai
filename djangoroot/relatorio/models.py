from django.db import models


# Create your models here.
class Relatorio(models.Model):
     descricao = models.CharField(max_length = 35)
     data = models.DateField()
     movimentacoes = models.ManyToManyField('movimentacao.Movimentacao')

     def __str__(self):
          output = f'Relatório do dia {self.data.day}/{self.data.month}/{self.data.year}: {self.descricao}'
          return output

'''
     É provável que este modelo mude, para que
     só tenha dados relacionados à movimentações
     de um único dia.

     Atualmente, os relatórios podem arquivar
     movimentações de diferentes dias.
'''