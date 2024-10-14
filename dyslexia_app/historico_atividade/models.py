from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class HistoricoAtividade(models.Model):
    atividade = models.ForeignKey('atividades.Atividade', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    erros = models.IntegerField()
    
    def __str__(self):
        return f"Histórico de {self.atividade.pre_video} realizado por {self.usuario.username}"
    
    @property
    def tempo_duracao(self):
        
        from datetime import datetime
        hora_inicial_dt = datetime.combine(self.data, self.hora_inicial)
        hora_final_dt = datetime.combine(self.data, self.hora_final)
        return hora_final_dt - hora_inicial_dt
    
    class Meta:
        db_table ="historico_atividade"