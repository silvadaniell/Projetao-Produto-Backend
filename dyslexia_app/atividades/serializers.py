from rest_framework import serializers
from .models import Atividade, CriancaAtividade

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'pre_video', 'content', 'dificuldade'] 

class CriancaAtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriancaAtividade
        fields = ['id', 'correto', 'tempo_resolucao', 'atividade']