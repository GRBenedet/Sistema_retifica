# Generated by Django 5.1.2 on 2024-11-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_notas_custototal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cpfcnpj',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='tel',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='notas',
            name='cod',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='pecas',
            name='cod',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='cod',
            field=models.BigIntegerField(),
        ),
    ]
