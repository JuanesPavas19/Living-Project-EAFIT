# Generated by Django 4.0.6 on 2022-10-22 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_dieta_recomendacion_rutina_recomendacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieta',
            name='info_dieta2',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='info_dieta3',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='recomendacion',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='info_rutina2',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='info_rutina3',
            field=models.CharField(max_length=750),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='recomendacion',
            field=models.CharField(max_length=750),
        ),
    ]
