from django.db import models

from QandA.helpers.modelhelpers import calculacodi


class TipusEspai(models.Model):
    # clau primària un codi de 5 caracters
    codi = models.CharField(
        "codi",
        max_length=5,
        default=calculacodi,
        editable=False,
        help_text="Codi intern",
        primary_key=True)

    text_ca = models.CharField(
        "Tipus espai (cat)",
        max_length=250,
        blank=False,
        help_text="Tipus espai en català")

    text_es = models.CharField(
        "Tipus espai (es)",
        max_length=250,
        blank=True,
        help_text="Tipus espai en castellà")

    text_en = models.CharField(
        "Tipus espai (en)",
        max_length=250,
        blank=True,
        help_text="Tipus espai amb anglès")

    def __str__(self):
        return self.text_ca

    class Meta:
        verbose_name = "tipus d'espai"
        verbose_name_plural = "tipus d'espais"
        ordering = ["text_ca"]

