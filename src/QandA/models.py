from decimal import Decimal
from django.db import models

from espais.models import TipusEspai
from accessibilitats.models import Discapacitat
from .helpers.modelhelpers import calculacodi
from django.utils.text import Truncator
from django.core.validators import MinValueValidator, MaxValueValidator
from math import isclose


class AgrupacioPreguntes(models.Model):

    # clau primària un codi de 5 caracters
    codi = models.CharField(
        "codi",
        max_length=5,
        editable=False,
        default=calculacodi,
        help_text="Codi intern",
        primary_key=True)

    tipusespai = models.ForeignKey(
        to=TipusEspai,
        verbose_name="Tipus espai",
        editable=False,
        help_text="A quin tipus espai pertany",
        on_delete=models.RESTRICT
    )

    order = models.IntegerField(
        "Codi ordenació",
        help_text="Utilitza aquest número per ordenar les agrupacions"
    )

    text_ca = models.CharField(
        "Pregunta (cat)",
        max_length=250,
        blank=False,
        help_text="Pregunta en català")

    text_es = models.CharField(
        "Pregunta (es)",
        max_length=250,
        blank=True,
        help_text="Pregunta en castellà")

    text_en = models.CharField(
        "Pregunta (en)",
        max_length=250,
        blank=True,
        help_text="Pregunta amb anglès")

    def __str__(self):
        return f"{self.tipusespai} - {self.text_ca}"

    class Meta:
        order_with_respect_to = "tipusespai"
        unique_together = ['tipusespai', 'order']
        verbose_name = "agrupació de preguntes"
        verbose_name_plural = "agrupacions de preguntes"


class Pregunta(models.Model):

    # clau primària un codi de 5 caracters
    codi = models.CharField(
        "codi",
        max_length=5,
        editable=False,
        default=calculacodi,
        help_text="Codi intern",
        primary_key=True)

    text_ca = models.CharField(
        "Pregunta (cat)",
        max_length=250,
        blank=False,
        help_text="Pregunta en català")

    text_es = models.CharField(
        "Pregunta (es)",
        max_length=250,
        blank=True,
        help_text="Pregunta en castellà")

    text_en = models.CharField(
        "Pregunta (en)",
        max_length=250,
        blank=True,
        help_text="Pregunta amb anglès")

    help_text_ca = models.CharField(
        "Text ajuda (cat)",
        max_length=250,
        blank=False,
        help_text="Text ajuda en català")

    help_text_es = models.CharField(
        "Text ajuda (es)",
        max_length=250,
        blank=True,
        help_text="Text ajuda en castellà")

    help_text_en = models.CharField(
        "Text ajuda (en)",
        max_length=250,
        blank=True,
        help_text="Text ajuda amb anglès")

    imatge = models.ImageField(
        "Il·lustració de la pregunta",
        blank=True,
        null=True,
        upload_to='QandA',
        help_text="""
            Atenció! Aquesta aplicació és inclusiva, la imatge no té
            text alternatiu i, per tant, ha de ser una ajuda opcional
            a l'hora de plantejar la pregunta"""
    )

    agrupaciopreguntes = models.ManyToManyField(
        "AgrupacioPreguntes",
        through='PreguntaDinsTipusEspai')

    def __str__(self):
        return self.text_ca

    class Meta:
        verbose_name_plural = "preguntes"
        verbose_name = "preguntes"
        ordering = ['text_ca']


class Resposta(models.Model):

    # clau primària un codi de 5 caracters
    codi = models.CharField(
        "codi",
        max_length=30,
        editable=False,
        default=calculacodi,
        help_text="Codi intern",
        primary_key=True)

    # fk a pregunta
    pregunta = models.ForeignKey(
        to=Pregunta,
        verbose_name="Pregunta",
        editable=False,
        help_text="Pregunta",
        on_delete=models.RESTRICT
    )

    order = models.IntegerField(
        "Codi ordenació",
        help_text="Utilitza aquest número per ordenar les respostes"
    )

    # text
    text_ca = models.CharField(
        "Resposta (cat)",
        max_length=250,
        blank=False,
        help_text="Resposta en català")

    text_es = models.CharField(
        "Resposta (es)",
        max_length=250,
        blank=True,
        help_text="Resposta en castellà")

    text_en = models.CharField(
        "Resposta (en)",
        max_length=250,
        blank=True,
        help_text="Resposta amb anglès")

    # imatge per il·lustrar la opció de resposta
    imatge = models.ImageField(
        "Il·lustració de la resposta",
        blank=True,
        null=True,
        upload_to='QandA',
        help_text="""
            Atenció! Aquesta aplicació és inclusiva, la imatge no té
            text alternatiu i, per tant, ha de ser una ajuda opcional
            a l'hora de plantejar la resposta"""
    )

    class Meta:
        order_with_respect_to = "pregunta"
        unique_together = ['pregunta', 'order']
        verbose_name = "resposta"
        verbose_name_plural = "respostes"

    def __str__(self):
        return self.text_ca


class PreguntaDinsTipusEspai(models.Model):

    agrupaciopreguntes = models.ForeignKey(
        to=AgrupacioPreguntes,
        verbose_name="Secció",
        help_text="Dins un tipus d'espai les preguntes s'agrupen en seccions",
        on_delete=models.RESTRICT,
    )

    tipusespai_cache = models.ForeignKey(
        to=TipusEspai,
        verbose_name="Tipus espai",
        editable=False,
        help_text="A quin tipus espai pertany",
        on_delete=models.RESTRICT
    )

    pregunta = models.ForeignKey(
        to=Pregunta,
        verbose_name="Pregunta",
        help_text="Pregunta",
        on_delete=models.RESTRICT
    )

    order = models.IntegerField(
        "Codi ordenació",
        help_text="Utilitza aquest número per ordenar les respostes"
    )

    class Importancia(models.IntegerChoices):
        ALTA = 3
        MITJA = 2
        BAIXA = 1

    importancia = models.IntegerField(
        verbose_name="Importància",
        help_text="Rellevància de la pregunta en aquest tipus d'espai",
        choices=Importancia.choices
    )

    class Meta:
        order_with_respect_to = "agrupaciopreguntes"
        unique_together = ['agrupaciopreguntes', 'order']

    def __str__(self):
        agrupacio = Truncator(self.agrupaciopreguntes).words(10)
        return f"{agrupacio} - {self.pregunta}"

    def save(self, *args, **kwargs):
        self.tipusespai_cache = self.agrupaciopreguntes.tipusespai
        super().save(*args, **kwargs)


class PuntuacioMaxima(models.Model):
    """
    Donada una pregunta i una discapacitat tenim un valor màxim dels punts
    que un espai pot obtenir en aquella pregunta per aquella discapacitat.

    La suma de totes les puntuacions serà sempre 100.

    Exemple 1:
        Q: HUTS, L'establiment es troba clarament senyalitzat? (importància 3)
        discapacitat : visual
        Afectació: 1.00
        afectacio_x_importancia: 3 (3 * 1.0)
        puntuacio_sense_arrodonir: 6.9% (3 / 43.25)
        puntuació: 5 (decidit per BIM)

    Exemple 2:
        Q: HUTS, L'establiment es troba clarament senyalitzat? (importància 3)
        discapacitat : auditiu
        Afectació: 0.25
        afectacio_x_importancia: 0.75 (3 * 0.25)
        puntuacio_sense_arrodonir: 2.9% (0.75 / 43.25)
        puntuació: 3 (decidit per BIM)

    Nota:
        43.25 és la suma de les afectacio_x_importancia de totes les
        afectacions d'una discapacitat en un tipus d'espai.

    Nota - ToDo:
        Caldria sobreescriure el save per tal que calculi:
            afectacio_x_importancia
            puntuacio_sense_arrodonir
            puntuacio
        quan aquests camps no tinguin valor
    """

    preguntadinstipusespai = models.ForeignKey(
        to=PreguntaDinsTipusEspai,
        verbose_name="Pregunta",
        editable=True,
        help_text="Pregunta dins una agrupació de preguntes",
        on_delete=models.CASCADE
    )

    tipusespai_cache = models.ForeignKey(
        to=TipusEspai,
        verbose_name="Tipus espai",
        editable=False,
        help_text="A quin tipus espai pertany",
        on_delete=models.RESTRICT
    )

    discapacitat = models.ForeignKey(
        to=Discapacitat,
        verbose_name="Discapacitat",
        editable=True,
        help_text="Aplicat a certa discapacitat",
        on_delete=models.CASCADE
    )

    afectacio = models.DecimalField(
        verbose_name="Percentatge d'afectació",
        max_digits=3,
        decimal_places=2,
        default=Decimal(0),
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
        help_text=(
            "Percentatge d'afectació d'aquesta pregunta a una discapacitat"
            "Entrar un número amb dos decimals. Sol ser 0.00, 0.25, 0.50 o "
            "1.00."
        ),
    )

    afectacio_x_importancia = models.FloatField(
        verbose_name="Afectacio x importancia",
        editable=False,
        help_text=(
            "Resultat de multiplicar l'afectació per la seva importància."
        ),
    )

    punts_sense_arrodonir = models.FloatField(
        verbose_name="Puntuació de la resposta (s/100)",
        editable=False,
        help_text=(
            "Puntuació ponderada sobre 100 amb decimals."
        ),
    )

    punts = models.IntegerField(
        verbose_name="Puntuació de la resposta",
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text=(
            "Puntuació final d'una resposta per a una discapacitat. "
            "La suma de totes les puntuacions per un tipus d'espai i"
            " discapacitat ha de ser 100."
        ),
    )

    def __str__(self):
        return str( self.preguntadinstipusespai )

    def save(self, *args, **kwargs):

        # Recalculem: afectacio_x_importancia
        tipusespai = (
            self
            .preguntadinstipusespai
            .agrupaciopreguntes
            .tipusespai)

        self.tipusespai_cache = tipusespai

        self.afectacio_x_importancia = float(
            float(self.afectacio) *
            float(self.preguntadinstipusespai.importancia)
        )

        # Desem
        super().save(*args, **kwargs)

        # Recalculem: punts_sense_arrodonir
        totes_les_respostes_de_la_discapacitat = (
            tipusespai.
            puntuaciomaxima_set.
            filter(discapacitat=self.discapacitat)
        )

        total_punts_de_la_discapacitat = sum(
            puntmax.afectacio_x_importancia
            for puntmax
            in totes_les_respostes_de_la_discapacitat
        )

        repartits = 0.
        for item in totes_les_respostes_de_la_discapacitat:
            punts = (
                100. * item.afectacio_x_importancia
                /
                float(total_punts_de_la_discapacitat)
            )
            punts_1decimal = round(punts, 1)

            # fem update per no disparar signals ni saves
            (
                totes_les_respostes_de_la_discapacitat
                .filter(pk=item.pk)
                .update(punts_sense_arrodonir=punts_1decimal)  # <-- Update
            )
            repartits += punts

        # safety check, ha de sumar 100.
        assert isclose(100.0, repartits, abs_tol=1e-7)


class AportacioResposta(models.Model):
    """
    Donada una resposta ens diu quin percentatge de la puntuació s'obtè
    si la regunta es repon amb aquesta resposta.
    """

    preguntadinstipusespai = models.ForeignKey(
        to=PreguntaDinsTipusEspai,
        verbose_name="Pregunta",
        editable=True,
        help_text="Pregunta associada una agrupació de preguntes",
        on_delete=models.CASCADE
    )

    resposta = models.ForeignKey(
        to=Resposta,
        verbose_name="Resposta",
        editable=True,
        help_text="Aplicat a certa resposta",
        on_delete=models.CASCADE
    )

    percentatge_aportacio = models.DecimalField(
        verbose_name="Percentatge d'aportació al resultat final",
        max_digits=2,
        decimal_places=1,
        default=Decimal(0),
        validators=[MinValueValidator(0.1), MaxValueValidator(1.0)],
        help_text=(
            "Valor del 0.1 al 1.00 quen ens indica quin percentatge de la "
            "puntuació aporta aquesta resposta al resultat final"
            "(normalment 1.0 ó 0.5) Si aporta 0 llavors no s'ha d'"
            "informar aquí."
        ),
    )
