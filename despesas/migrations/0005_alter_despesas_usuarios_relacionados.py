# Generated by Django 4.1.3 on 2022-12-10 01:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('despesas', '0004_remove_despesas_usuario_criador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesas',
            name='usuarios_relacionados',
            field=models.ManyToManyField(related_name='relacionados', to=settings.AUTH_USER_MODEL),
        ),
    ]
