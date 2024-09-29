from django.db import models
from django.contrib.auth.models import User


class AtividadeABC(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    atividades_concluidas = models.IntegerField()
    atividades_com_erro = models.IntegerField()
    erros_por_atividade = models.TextField()
    
    def __str__(self):
        return f'AtividadeABC - {self.usuario_id}'
    
class AtividadeSilabas(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    atividades_concluidas = models.IntegerField()
    atividades_com_erro = models.IntegerField()
    erros_por_atividade = models.TextField()

    def __str__(self):
        return f'AtividadeSilabas - {self.usuario_id}'
    
class AtividadePalavras(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    atividades_concluidas = models.IntegerField()
    atividades_com_erro = models.IntegerField()
    erros_por_atividade = models.TextField()

    def __str__(self):
        return f'AtividadePalavras - {self.usuario_id}'

