# Generated by Django 2.2.3 on 2019-07-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_auto_20190716_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='preguntas',
            name='pregunta_abrebiacion',
            field=models.CharField(default='N/A', max_length=20, verbose_name='Abrebiacion'),
        ),
    ]