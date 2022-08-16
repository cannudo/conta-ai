from django.db import models

# Create your models here.
class Lancamento(models.Model):
    titulo = models.CharField(max_length = 20, help_text = 'É uma breve descrição do lançamento.')
    entrada = models.BooleanField()
    descricao = models.TextField(max_length = 45, help_text = 'É uma descrição detalhada do lançamento.')
    valor = models.DecimalField(decimal_places = 2, max_digits = 10)

    def __str__(self):
        return (("Entrada de" if self.entrada else "Saída de") + " R$ " + str(self.valor) + " — " + self.titulo + ": " + self.descricao)

    # TODO: Arrumar esse str e pesquisar sobre o max_digits do DecimalField