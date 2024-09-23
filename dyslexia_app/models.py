from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerFIeld()

class Historia(models.Model):
    qtd_atividades = models.IntegerField()

class Atividade(models.Model):
    resolution_time = models.TimeField()
    correct = models.BooleanField()

    kid = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )

    historia = models.OneToOneField(
        Historia,
        on_delete=models.CASCADE
    )

