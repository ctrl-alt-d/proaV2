# Generated by Django 4.2 on 2023-05-28 13:55

import QandA.helpers.modelhelpers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discapacitat',
            fields=[
                ('codi', models.TextField(default=QandA.helpers.modelhelpers.calculacodi, editable=False, help_text='Codi intern', max_length=12, primary_key=True, serialize=False, verbose_name='codi')),
                ('text_ca', models.TextField(help_text='Discapacitat en català', max_length='50', verbose_name='Discapacitat (cat)')),
                ('text_es', models.TextField(blank=True, help_text='Discapacitat en castellà', max_length='50', verbose_name='Discapacitat (es)')),
                ('text_en', models.TextField(blank=True, help_text='Discapacitat amb anglès', max_length='50', verbose_name='Discapacitat (en)')),
            ],
            options={
                'verbose_name': 'discapacitat',
                'verbose_name_plural': 'Discapacitats',
            },
        ),
    ]
