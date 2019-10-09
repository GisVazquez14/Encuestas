# Generated by Django 2.2.3 on 2019-07-19 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encuestas', '0003_preguntas_pregunta_abrebiacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleccion',
            name='user_creo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]