# Generated by Django 5.1.2 on 2024-11-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_notas'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='custototal',
            field=models.FloatField(blank=True, null=True),
        ),
    ]