from movimentacao.models import Movimentacao
from rest_framework import serializers

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimentacao
        fields = ['titulo', 'descricao', 'entrada', 'valor', 'data']