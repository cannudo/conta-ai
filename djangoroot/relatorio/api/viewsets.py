from rest_framework.viewsets import ModelViewSet
from .serializers import RelatorioSerializer
from relatorio.models import Relatorio


class RelatorioViewSet(ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer