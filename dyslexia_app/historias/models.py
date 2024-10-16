from django.db import models
from atividades.models import Atividade 
class Historia(models.Model):
    # qtd_atividades = models.IntegerField()
    
    conteudo_atividade = models.TextField()
    id_atividade = models.ManyToManyField(Atividade, related_name="historias")
    
    class Meta:
        db_table ="historias"
