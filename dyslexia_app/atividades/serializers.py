from rest_framework import serializers
from .models import AtividadeABC, AtividadeSilabas, AtividadePalavras

class AtividadeABCSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeABC
        fields = ['id', 'usuario_id', 'atividades_concluidas', 'atividades_com_erro', 'erros_por_atividade']

class AtividadeSilabasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadeSilabas
        fields = ['id', 'usuario_id', 'atividades_concluidas', 'atividades_com_erro', 'erros_por_atividade']

class AtividadePalavrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadePalavras
        fields = ['id', 'usuario_id', 'atividades_concluidas', 'atividades_com_erro', 'erros_por_atividade']
