from fluxodecaixa.models import FluxoDeCaixa
from rest_framework.serializers import ModelSerializer

class FluxoDeCaixaSerializer(ModelSerializer):
    class Meta:
        model = FluxoDeCaixa
        fields = ['titulo', 'descricao', 'relatorios']