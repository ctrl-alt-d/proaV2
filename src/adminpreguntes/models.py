from django.db import models
from QandA.models import Pregunta, PreguntaDinsTipusEspai
from django.utils.text import Truncator

from espais.models import TipusEspai


class P_Pregunta_i_Respostes(Pregunta):
    class Meta:
        proxy = True
        verbose_name = "Pregunta i respostes"
        verbose_name_plural = "Preguntes i respostes"

    def __str__(self):
        n_respostes = self.resposta_set.count()
        n_tipus_espais = (
            self
            .preguntadinstipusespai_set
            .count()
        )

        return (
            self.text_ca +
            f" ({n_respostes} respostes" +
            f" s'utilitza a {n_tipus_espais} espais)"
        )


class P_TipusEspai_AgrupacionsP(TipusEspai):
    class Meta:
        proxy = True
        verbose_name = "Tipus espai i seccions"
        verbose_name_plural = "Tipus espai i seccions"

    def __str__(self):
        n_agrupacions = self.agrupaciopreguntes_set.count()
        return (
            self.text_ca +
            f" ({n_agrupacions} seccions)"
        )


class P_TipusEspai_Preguntes(TipusEspai):
    class Meta:
        proxy = True
        verbose_name = "Tipus espai i preguntes"
        verbose_name_plural = "Tipus espai i preguntes"

    def __str__(self):
        n_agrupacions = self.agrupaciopreguntes_set.count()
        n_preguntes = sum(
            a.preguntadinstipusespai_set.count()
            for a in self.agrupaciopreguntes_set.all()
        )
        return (
            self.text_ca +
            f" ({n_preguntes} preguntes en {n_agrupacions} seccions)"
        )


class P_TipusEspai_PuntuacionsMaximes_Visual(TipusEspai):
    class Meta:
        proxy = True
        verbose_name = "Tipus espai i puntuacions visual max."
        verbose_name_plural = "Tipus espais i puntuacions visual màx."


class P_PreguntaDinsTipusEspai_Exclusions(PreguntaDinsTipusEspai):
    class Meta:
        proxy = True
        verbose_name = "Exclusions"
        verbose_name_plural = "Exclusions"
        ordering = ["tipusespai_cache",  "order", ]

    def __str__(self):
        n_exclusions = self.exclusio_set.count()
        agrupacio = Truncator(self.agrupaciopreguntes).words(10)
        n_exclusions_txt = (
            f" 🚫 {n_exclusions} exclusió 🚫" if n_exclusions == 1 else
            f" 🚫 {n_exclusions} exclusins 🚫" if n_exclusions > 1 else
            ""
        )
        return f"{agrupacio} - {self.pregunta} {n_exclusions_txt}"
    