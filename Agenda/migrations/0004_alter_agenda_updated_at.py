# Generated by Django 4.0.4 on 2022-09-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agenda', '0003_remove_agenda_rotas_veiculos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Modificado em:'),
        ),
    ]
