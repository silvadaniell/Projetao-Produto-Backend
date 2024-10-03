from rest_framework import viewsets
from .models import Atividades
from .serializers import AtividadesSerializer, CriancaAtividadeSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = AtividadesSerializer

class CriancaAtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = CriancaAtividadeSerializer