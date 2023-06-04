# Generated by Django 4.2 on 2023-06-04 13:35

import QandA.helpers.modelhelpers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipusEspai',
            fields=[
                ('codi', models.CharField(default=QandA.helpers.modelhelpers.calculacodi, editable=False, help_text='Codi intern', max_length=5, primary_key=True, serialize=False, verbose_name='codi')),
                ('text_ca', models.CharField(help_text='Tipus espai en català', max_length=250, verbose_name='Tipus espai (cat)')),
                ('text_es', models.CharField(blank=True, help_text='Tipus espai en castellà', max_length=250, verbose_name='Tipus espai (es)')),
                ('text_en', models.CharField(blank=True, help_text='Tipus espai amb anglès', max_length=250, verbose_name='Tipus espai (en)')),
            ],
            options={
                'verbose_name': "tipus d'espai",
                'verbose_name_plural': "tipus d'espais",
                'ordering': ['text_ca'],
            },
        ),
    ]