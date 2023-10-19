# Generated by Django 4.2.6 on 2023-10-19 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=255, verbose_name='NOME COMPLETO')),
                ('cpf', models.CharField(help_text='000.000.000-00', max_length=255, verbose_name='CPF')),
                ('fone', models.CharField(help_text='Dê preferência ao número do Whatsapp', max_length=15, verbose_name='TELEFONE')),
                ('doc_inserido', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='DocumentoContrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('documento', models.FileField(max_length=2000, upload_to='documento_contrato', verbose_name='Documento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_documentos', to='cliente.pessoa')),
            ],
            options={
                'ordering': ['cliente'],
            },
        ),
    ]
