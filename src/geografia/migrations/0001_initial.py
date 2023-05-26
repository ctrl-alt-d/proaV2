# Generated by Django 4.2 on 2023-05-26 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comarca',
            fields=[
                ('codi', models.CharField(help_text='Codi del Consell Comarcal', max_length=2, primary_key=True, serialize=False, unique=True, verbose_name='Codi del Consell Comarcal')),
                ('nom', models.CharField(help_text='Nom del Consell Comarcal', max_length=100, verbose_name='Nom del Consell Comarcal')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('codi', models.CharField(help_text='Codi de província', max_length=2, primary_key=True, serialize=False, unique=True, verbose_name='Codi de província')),
                ('nom', models.CharField(help_text='Nom de la província', max_length=100, verbose_name='Nom de la província')),
            ],
        ),
        migrations.CreateModel(
            name='Municipi',
            fields=[
                ('codi', models.CharField(help_text='Codi de Municipi', max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Codi de Municipi')),
                ('nom', models.CharField(help_text='Nom del Municipi', max_length=100, verbose_name='Nom del Municipi')),
                ('nom_comarca', models.CharField(help_text='Nom del Consell Comarcal', max_length=100, verbose_name='Nom del Consell Comarcal')),
                ('nom_provincia', models.CharField(help_text='Nom de la Província', max_length=100, verbose_name='Nom de la Província')),
                ('codi_comarca', models.ForeignKey(help_text='Codi de Consell Comarcal aa que pertany el municipi', on_delete=django.db.models.deletion.CASCADE, to='geografia.comarca', verbose_name='Consell Comarcal')),
                ('codi_provincia', models.ForeignKey(help_text='Codi de Província al que pertany el municipi', on_delete=django.db.models.deletion.CASCADE, to='geografia.provincia', verbose_name='Província')),
            ],
        ),
    ]