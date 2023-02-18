from rest_framework.viewsets import ModelViewSet
from .serializers import MovimentacaoSerializer
from movimentacao.models import Movimentacao

class MovimentacaoViewSet(ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer