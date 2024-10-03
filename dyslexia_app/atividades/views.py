from rest_framework import viewsets
from .models import Atividade
from .serializers import AtividadeSerializer, CriancaAtividadeSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class CriancaAtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = CriancaAtividadeSerializer