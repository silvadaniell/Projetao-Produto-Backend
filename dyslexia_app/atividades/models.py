from django.db import models
from django.contrib.auth.models import Historia, User

class Atividade(models.Model):
    pre_video = models.CharField() #pre video link
    content = models.JSONField()
    dificuldade = models.IntegerField()

    historia = models.OneToOneField(
        Historia,
        on_delete=models.CASCADE
    )

class CriancaAtividade(models.Model):
    crianca = models.ForeignKey(to=User)
    atividade = models.ForeignKey(to=Atividade)
    correto = models.BooleanField()
    tempo_resolucao = models.TimeField()