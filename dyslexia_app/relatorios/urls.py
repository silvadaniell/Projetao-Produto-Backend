from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'atividades_abc', views.AtividadeABCViewSet)
router.register(r'atividades_silabas', views.AtividadeSilabasViewSet)
router.register(r'atividades_palavras', views.AtividadePalavrasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
