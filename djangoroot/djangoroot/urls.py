from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken .views import obtain_auth_token

from movimentacao.api.viewsets import MovimentacaoViewSet
from relatorio.api.viewsets import RelatorioViewSet
from fluxodecaixa.api.viewsets import FluxoDeCaixaViewSet


router = routers.DefaultRouter()

router.register(r'movimentacao', MovimentacaoViewSet) # Django, adicione suporte à essa URL
router.register(r'relatorio', RelatorioViewSet)
router.register(r'fluxosdecaixa', FluxoDeCaixaViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)), # rotas definidas no DefaultRouter() 
    path('admin/', admin.site.urls)
]