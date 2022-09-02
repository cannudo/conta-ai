from django.db import models

# Create your models here.
class FluxoDeCaixa(models.Model):
    data = models.DateField()

    def getLancamentos(self):
        return self.lancamento_set.all()

    def __str__(self):
        return "Fluxo do dia %d/%d/%d" % (self.data.day, self.data.month, self.data.year)