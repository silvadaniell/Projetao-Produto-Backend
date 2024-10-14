from django.db import models

class Historia(models.Model):
    qtd_atividades = models.IntegerField()
    
    # definir os videos e a disposicao das atividades
    class Meta:
        db_table ="historias"
