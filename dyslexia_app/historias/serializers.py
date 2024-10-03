from rest_framework import serializers
from .models import Historia

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['id', 'qtd_atividades']