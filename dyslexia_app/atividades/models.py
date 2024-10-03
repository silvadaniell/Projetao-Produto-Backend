from django.db import models
from django.contrib.auth.models import User

class Atividade(models.Model):
    pre_video = models.CharField(max_length=255) #pre video link
    content = models.JSONField()
    dificuldade = models.IntegerField()

    historia = models.OneToOneField(
        'historias.Historia',
        on_delete=models.CASCADE
    )

class CriancaAtividade(models.Model):
    crianca = models.ForeignKey(User, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    correto = models.BooleanField()
    tempo_resolucao = models.TimeField()