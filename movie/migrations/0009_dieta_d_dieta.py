# Generated by Django 4.0.6 on 2022-11-07 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_rename_recomendacion_rutina_previo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='d_dieta',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
