# Generated by Django 5.1.2 on 2024-11-06 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_alter_clientes_cpfcnpj_alter_clientes_tel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='prod',
        ),
        migrations.RemoveField(
            model_name='orcamentos',
            name='ativos_servicos',
        ),
        migrations.RemoveField(
            model_name='orcamentos',
            name='buy_pecas',
        ),
        migrations.RemoveField(
            model_name='pecas',
            name='aplic',
        ),
        migrations.AddField(
            model_name='notas',
            name='prod',
            field=models.ManyToManyField(to='principal.pecas'),
        ),
        migrations.AddField(
            model_name='orcamentos',
            name='ativos_servicos',
            field=models.ManyToManyField(blank=True, null=True, to='principal.servicos'),
        ),
        migrations.AddField(
            model_name='orcamentos',
            name='buy_pecas',
            field=models.ManyToManyField(blank=True, null=True, to='principal.pecas'),
        ),
        migrations.AddField(
            model_name='pecas',
            name='aplic',
            field=models.ManyToManyField(to='principal.motor'),
        ),
    ]