from rest_framework import viewsets
from .models import AtividadeABC, AtividadeSilabas, AtividadePalavras
from .serializers import AtividadeABCSerializer, AtividadeSilabasSerializer, AtividadePalavrasSerializer

class AtividadeABCViewSet(viewsets.ModelViewSet):
    queryset = AtividadeABC.objects.all()
    serializer_class = AtividadeABCSerializer

class AtividadeSilabasViewSet(viewsets.ModelViewSet):
    queryset = AtividadeSilabas.objects.all()
    serializer_class = AtividadeSilabasSerializer

class AtividadePalavrasViewSet(viewsets.ModelViewSet):
    queryset = AtividadePalavras.objects.all()
    serializer_class = AtividadePalavrasSerializer
