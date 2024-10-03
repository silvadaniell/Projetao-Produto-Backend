from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerFIeld()

class Historia(models.Model):
    qtd_atividades = models.IntegerField()

    # definir os videos e a disposicao das atividades

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