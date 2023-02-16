from relatorio.models import Relatorio
from rest_framework.serializers import ModelSerializer

class RelatorioSerializer(ModelSerializer):
    class Meta:
        model = Relatorio
        fields = ['descricao', 'data', 'movimentacoes']