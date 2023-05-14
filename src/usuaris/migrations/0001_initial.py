# Generated by Django 4.2 on 2023-05-14 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=60, verbose_name='Nom de la persona de contacte')),
                ('cognoms', models.CharField(blank=True, max_length=120, verbose_name='Cognom de la persona de contacte')),
                ('organitzacio', models.CharField(blank=True, max_length=120, verbose_name='Organització')),
                ('telefon', models.CharField(blank=True, help_text='Telèfon de contacte ( telf. Professional)', max_length=60, verbose_name='Telèfon de contacte')),
                ('usuari', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cognoms', 'nom'],
            },
        ),
    ]