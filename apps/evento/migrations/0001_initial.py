# Generated by Django 3.0.8 on 2020-07-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '01 - Cadastro de Evento',
            },
        ),
    ]
