# Generated by Django 4.2 on 2023-07-12 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('espais', '0001_initial'),
        ('QandA', '0001_initial'),
        ('accessibilitats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntuaciomaxima',
            name='tipusespai_cache',
            field=models.ForeignKey(editable=False, help_text='A quin tipus espai pertany', on_delete=django.db.models.deletion.RESTRICT, to='espais.tipusespai', verbose_name='Tipus espai'),
        ),
        migrations.AddField(
            model_name='preguntadinstipusespai',
            name='agrupaciopreguntes',
            field=models.ForeignKey(help_text="Dins un tipus d'espai les preguntes s'agrupen en seccions", on_delete=django.db.models.deletion.RESTRICT, to='QandA.agrupaciopreguntes', verbose_name='Secció'),
        ),
        migrations.AddField(
            model_name='preguntadinstipusespai',
            name='pregunta',
            field=models.ForeignKey(help_text='Pregunta', on_delete=django.db.models.deletion.RESTRICT, to='QandA.pregunta', verbose_name='Pregunta'),
        ),
        migrations.AddField(
            model_name='preguntadinstipusespai',
            name='tipusespai_cache',
            field=models.ForeignKey(editable=False, help_text='A quin tipus espai pertany', on_delete=django.db.models.deletion.RESTRICT, to='espais.tipusespai', verbose_name='Tipus espai'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='agrupaciopreguntes',
            field=models.ManyToManyField(through='QandA.PreguntaDinsTipusEspai', to='QandA.agrupaciopreguntes'),
        ),
        migrations.AddField(
            model_name='exclusio',
            name='discapacitat',
            field=models.ForeignKey(help_text='Aplicat a certa discapacitat', on_delete=django.db.models.deletion.CASCADE, to='accessibilitats.discapacitat', verbose_name='Discapacitat'),
        ),
        migrations.AddField(
            model_name='exclusio',
            name='preguntadinstipusespai',
            field=models.ForeignKey(help_text='Pregunta dins una agrupació de preguntes', on_delete=django.db.models.deletion.CASCADE, to='QandA.preguntadinstipusespai', verbose_name='Pregunta'),
        ),
        migrations.AddField(
            model_name='exclusio',
            name='resposta',
            field=models.ForeignKey(help_text='Aplicat a certa discapacitat', on_delete=django.db.models.deletion.CASCADE, to='QandA.resposta', verbose_name='Discapacitat'),
        ),
        migrations.AddField(
            model_name='exclusio',
            name='tipusespai_cache',
            field=models.ForeignKey(editable=False, help_text='A quin tipus espai pertany', on_delete=django.db.models.deletion.RESTRICT, to='espais.tipusespai', verbose_name='Tipus espai'),
        ),
        migrations.AddField(
            model_name='aportacioresposta',
            name='preguntadinstipusespai',
            field=models.ForeignKey(help_text='Pregunta associada una agrupació de preguntes', on_delete=django.db.models.deletion.CASCADE, to='QandA.preguntadinstipusespai', verbose_name='Pregunta'),
        ),
        migrations.AddField(
            model_name='aportacioresposta',
            name='resposta',
            field=models.ForeignKey(help_text='Aplicat a certa resposta', on_delete=django.db.models.deletion.CASCADE, to='QandA.resposta', verbose_name='Resposta'),
        ),
        migrations.AddField(
            model_name='agrupaciopreguntes',
            name='tipusespai',
            field=models.ForeignKey(editable=False, help_text='A quin tipus espai pertany', on_delete=django.db.models.deletion.RESTRICT, to='espais.tipusespai', verbose_name='Tipus espai'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='resposta',
            order_with_respect_to='pregunta',
        ),
        migrations.AlterUniqueTogether(
            name='resposta',
            unique_together={('pregunta', 'order')},
        ),
        migrations.AlterOrderWithRespectTo(
            name='preguntadinstipusespai',
            order_with_respect_to='agrupaciopreguntes',
        ),
        migrations.AlterUniqueTogether(
            name='preguntadinstipusespai',
            unique_together={('agrupaciopreguntes', 'order')},
        ),
        migrations.AlterOrderWithRespectTo(
            name='agrupaciopreguntes',
            order_with_respect_to='tipusespai',
        ),
        migrations.AlterUniqueTogether(
            name='agrupaciopreguntes',
            unique_together={('tipusespai', 'order')},
        ),
    ]