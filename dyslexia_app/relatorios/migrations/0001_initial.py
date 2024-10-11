# Generated by Django 5.1.1 on 2024-10-10 23:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeABC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividades_concluidas', models.IntegerField()),
                ('atividades_com_erro', models.IntegerField()),
                ('erros_por_atividade', models.TextField()),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AtividadePalavras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividades_concluidas', models.IntegerField()),
                ('atividades_com_erro', models.IntegerField()),
                ('erros_por_atividade', models.TextField()),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AtividadeSilabas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividades_concluidas', models.IntegerField()),
                ('atividades_com_erro', models.IntegerField()),
                ('erros_por_atividade', models.TextField()),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
