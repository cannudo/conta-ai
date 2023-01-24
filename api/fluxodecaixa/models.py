from django.db import models

# Create your models here.
class FluxoDeCaixa(models.Model):
    titulo = models.CharField(max_length = 45)
    descricao = models.CharField(max_length = 90, null = True, blank = True)
    relatorios = models.ManyToManyField('relatorio.Relatorio')

    def __str__(self):
        return "%s" % (self.titulo)