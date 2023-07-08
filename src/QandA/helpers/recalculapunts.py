from typing import List
from QandA.models import PuntuacioMaxima
from accessibilitats.models import Discapacitat
from espais.models import TipusEspai
from django.db.models import Sum


def recalcula(discapacitat: Discapacitat, tipusespai: TipusEspai) -> None:

    # Preparem funció get punts màxims per una discapacitat i tipus d'espai
    punts_maxims = _get_punts_maxims(discapacitat, tipusespai)

    # Informen punts arrodonint punts sense arrodonir però sense dixar-los a 0
    for puntuacio in punts_maxims:

        punt_arrodonit = int(round(puntuacio.punts_sense_arrodonir))

        # No volem dixar-los a 0
        if punt_arrodonit == 0:
            punt_arrodonit = 1

        _actualitza_punts(puntuacio, punt_arrodonit)

    # Un cop tots arrodonits mirem quan sobra
    total_punts_sense_arrodonir = sum(
        x.punts_sense_arrodonir
        for x in punts_maxims
    )
    total_punts = sum(
        x.punts
        for x in punts_maxims
    )

    sobrant = int(round(total_punts - total_punts_sense_arrodonir))

    # Algoritme molt millorable, pordriem repartir proporcional
    # als punts que ja tenen.

    # Decidim si hem de sumar o restar punts
    diferencial = -1 if sobrant > 0 else +1

    # Ordenem per començar a repartir el sobrant
    def clau(x): return -x.punts
    punts_ordenats = sorted(punts_maxims, key=clau)

    # Repartim el sobrant de punt en punt.
    for puntuacio in punts_ordenats:
        _actualitza_punts(puntuacio, puntuacio.punts + diferencial)
        sobrant += diferencial
        if not sobrant:
            break

    # Un cop repartit el sobrant, ha de sumar 100
    punts_bd = (
        tipusespai
        .puntuaciomaxima_set
        .filter(discapacitat=discapacitat)
        .aggregate(punts=Sum('punts'))
        ['punts']
    )

    if (punts_bd != 100):
        err = f"Els punts haurien de sumar 100 i sumen {punts_bd}"
        raise ValueError(err)


def _actualitza_punts(puntuacio: PuntuacioMaxima, punts: int) -> None:
    (
        PuntuacioMaxima
        .objects
        .filter(pk=puntuacio.pk)
        .update(punts=punts)
    )
    puntuacio.refresh_from_db()


def _get_punts_maxims(
        discapacitat: Discapacitat,
        tipusespai: TipusEspai
) -> List[PuntuacioMaxima]:
    return list(
        tipusespai
        .puntuaciomaxima_set
        .filter(discapacitat=discapacitat)
        .filter(punts_sense_arrodonir__gt=0)
    )
