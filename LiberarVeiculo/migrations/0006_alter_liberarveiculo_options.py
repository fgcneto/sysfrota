# Generated by Django 4.0.4 on 2022-10-27 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LiberarVeiculo', '0005_alter_liberarveiculo_confirmacao_chegada_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liberarveiculo',
            options={'ordering': ['agendamento'], 'verbose_name': 'Liberar Veículo', 'verbose_name_plural': 'Liberar Veículos'},
        ),
    ]