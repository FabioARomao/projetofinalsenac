# Generated by Django 2.2.12 on 2023-07-25 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_login_criado_pessoa_criado_produto_criado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='criado',
        ),
    ]