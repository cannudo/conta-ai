from rest_framework import viewsets
from movimentacao.models import Movimentacao
from movimentacao.serializers import MovimentacaoSerializer

class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer