# Generated by Django 5.1.1 on 2024-10-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_atividades', models.IntegerField()),
            ],
            options={
                'db_table': 'historias',
            },
        ),
    ]
