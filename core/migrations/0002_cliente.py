# Generated by Django 3.2.5 on 2021-11-25 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('data_nascimento', models.DateTimeField(verbose_name='Data de Nascimento')),
            ],
        ),
    ]
