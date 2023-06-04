from django.db import models
from QandA.models import Pregunta

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
