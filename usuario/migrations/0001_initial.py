# Generated by Django 4.1.3 on 2022-11-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('nome', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
