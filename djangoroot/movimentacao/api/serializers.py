from movimentacao.models import Movimentacao
from rest_framework.serializers import ModelSerializer

class MovimentacaoSerializer(ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ['titulo', 'descricao', 'entrada', 'valor', 'data']