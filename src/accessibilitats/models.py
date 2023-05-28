from django.db import models

from QandA.helpers.modelhelpers import calculacodi


class Discapacitat(models.Model):

    # clau primària un codi de 5 caracters
    codi = models.TextField(
        "codi",
        max_length=12,
        default=calculacodi,
        editable=False,
        help_text="Codi intern",
        primary_key=True)

    text_ca = models.TextField(
        "Discapacitat (cat)",
        max_length="50",
        blank=False,
        help_text="Discapacitat en català")

    text_es = models.TextField(
        "Discapacitat (es)",
        max_length="50",
        blank=True,
        help_text="Discapacitat en castellà")

    text_en = models.TextField(
        "Discapacitat (en)",
        max_length="50",
        blank=True,
        help_text="Discapacitat amb anglès")

    def __str__(self):
        return self.text_ca

    class Meta:
        verbose_name = "discapacitat"
        verbose_name_plural = "Discapacitats"
