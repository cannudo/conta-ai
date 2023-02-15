from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from movimentacao.api.viewsets import MovimentacaoViewSet

router = routers.DefaultRouter()

router.register(r'movimentacao', MovimentacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
