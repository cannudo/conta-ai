from django.test import TestCase
from .models import Lancamento
from fluxodecaixa.models import FluxoDeCaixa
from datetime import date


class LancamentoTestCase(TestCase):
    def setUp(self):
        f = FluxoDeCaixa.objects.create(data = date.today())
        l = Lancamento.objects.create(titulo = "Pix da Mary", entrada = True, descricao = "Mesada", valor = 250, fluxodecaixa = f)

    def test(self):
        test = Lancamento.objects.first()
        print(test)