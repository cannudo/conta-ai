from rest_framework.viewsets import ModelViewSet
from .serializers import FluxoDeCaixaSerializer
from fluxodecaixa.models import FluxoDeCaixa

class FluxoDeCaixaViewSet(ModelViewSet):
    queryset = FluxoDeCaixa.objects.all()
    serializer_class = FluxoDeCaixaSerializer