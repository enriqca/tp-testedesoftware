# Generated by Django 4.1.3 on 2022-11-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0002_despesas_usuario_criador_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesas',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='SaldoDespesas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('despesas', models.ManyToManyField(to='despesas.despesas')),
            ],
        ),
    ]