from rest_framework import serializers
from .models import HistoricoAtividade

class HistoricoAtividadeSerializer(serializers.ModelSerializer):
    atividade_nome = serializers.CharField(source='atividade.pre_video', read_only=True)
    usuario_nome = serializers.CharField(source='usuario.username', read_only=True)
    tempo_duracao = serializers.DurationField(read_only=True)
    
    class Meta:
        model = HistoricoAtividade
        fields = ['atividade', 'atividade_nome', 'usuario', 'usuario_nome', 'data', 'hora_inicial', 'hora_final', 'tempo_duracao', 'erros']