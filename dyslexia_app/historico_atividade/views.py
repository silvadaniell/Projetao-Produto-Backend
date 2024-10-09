from rest_framework import generics
from .models import HistoricoAtividade
from .serializers import HistoricoAtividadeSerializer
from rest_framework.permissions import IsAuthenticated

class HistoricoAtividadeListCreateView(generics.ListCreateAPIView):
    queryset = HistoricoAtividade.objects.all()
    serializer_class = HistoricoAtividadeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
