from django.db import models

# Create your models here.
class Movimentacao(models.Model):
    titulo = models.CharField(max_length = 35)
    descricao = models.TextField(max_length = 140, null = True)
    entrada = models.BooleanField(default = True)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        '''
            Essa não é a maneira mais funcional
            de se passar uma função no retorno
            de outra.

            Mas eu tentei.


            Alô @lrlucena !
        '''
        sinal = "↑" if (self.entrada) else "↓"
        output = sinal + f' R$ {self.valor} — {self.titulo} [{self.data.day}/{self.data.month}/{self.data.year}]'

        return output