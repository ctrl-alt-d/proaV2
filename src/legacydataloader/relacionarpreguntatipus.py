from typing import List
from QandA.helpers.modelhelpers import calculacodi
from QandA.models import AgrupacioPreguntes, AportacioResposta, Pregunta, PreguntaDinsTipusEspai, PuntuacioMaxima
from accessibilitats.models import Discapacitat
from estructures.constants import DiscapacitatsEnum
from legacydata.puntuacions import PuntuacioStruct, Puntuacions
from legacydata.tipusespais import GetTipusEspaisStructs
from legacydata.respostes import respostesdict


def relacionapreguntaambtipus():
    for tipus in GetTipusEspaisStructs():
        coditipusespai = tipus.codi
        puntuacions = Puntuacions[coditipusespai]

        preguntes = [
            (item[0], item[1][0])
            for item in tipus.preguntes.items()
            if item[0].startswith("f_")
        ]

        _relaciona(coditipusespai, preguntes, puntuacions)


def _relaciona(coditipusespai, preguntes, puntuacions: List[PuntuacioStruct]):
    agrupacio_anterior = None
    for codipregunta, textpregunta in preguntes:
        codicategoria = coditipusespai + "-" + codipregunta.split("_")[1]
        agrupacio = AgrupacioPreguntes.objects.get(pk=codicategoria)
        pregunta = Pregunta.objects.get(text_ca=textpregunta)
        puntuacio = next(x for x in puntuacions if x.codi == codipregunta)

        if agrupacio_anterior != agrupacio:
            order = agrupacio.order * 1000
            agrupacio_anterior = agrupacio

        preguntadinstipusespai = PreguntaDinsTipusEspai.objects.create(
            agrupaciopreguntes=agrupacio,
            pregunta=pregunta,
            importancia=puntuacio.importancia,
            order=order
        )

        order += 10

        _afegeix_puntuaciomaxima(
            preguntadinstipusespai, puntuacio)

        _afegeig_aportacioresposta(
            preguntadinstipusespai, puntuacio.r1, puntuacio.p1)

        _afegeig_aportacioresposta(
            preguntadinstipusespai, puntuacio.r2, puntuacio.p2)

        _afegeig_aportacioresposta(
            preguntadinstipusespai, puntuacio.r3, puntuacio.p3)


def _afegeix_puntuaciomaxima(
        preguntadinstipusespai: PreguntaDinsTipusEspai,
        puntuacio: PuntuacioStruct):
    """
    Es tracta de crear un PuntuacioMaxima x cada discapacitat
    """

    PuntuacioMaxima.objects.create(
        preguntadinstipusespai=preguntadinstipusespai,
        discapacitat=__get_disc(DiscapacitatsEnum.AUDITIU),
        afectacio=puntuacio.auditiu_pct,
        afectacio_x_importancia=0,
        punts_sense_arrodonir=0,
        punts=puntuacio.auditiu_punts,
    )

    PuntuacioMaxima.objects.create(
        preguntadinstipusespai=preguntadinstipusespai,
        discapacitat=__get_disc(DiscapacitatsEnum.CADIRADERODES),
        afectacio=puntuacio.cadira_pct,
        afectacio_x_importancia=0,
        punts_sense_arrodonir=0,
        punts=puntuacio.cadira_punts,
    )

    PuntuacioMaxima.objects.create(
        preguntadinstipusespai=preguntadinstipusespai,
        discapacitat=__get_disc(DiscapacitatsEnum.FAMILIAR),
        afectacio=puntuacio.familiar_pct,
        afectacio_x_importancia=0,
        punts_sense_arrodonir=0,
        punts=puntuacio.familiar_punts,
    )

    PuntuacioMaxima.objects.create(
        preguntadinstipusespai=preguntadinstipusespai,
        discapacitat=__get_disc(DiscapacitatsEnum.MOBILITATREDUIDA),
        afectacio=puntuacio.movilitat_pct,
        afectacio_x_importancia=0,
        punts_sense_arrodonir=0,
        punts=puntuacio.movilitat_punts,
    )

    PuntuacioMaxima.objects.create(
        preguntadinstipusespai=preguntadinstipusespai,
        discapacitat=__get_disc(DiscapacitatsEnum.VISUAL),
        afectacio=puntuacio.visual_pct,
        afectacio_x_importancia=0,
        punts_sense_arrodonir=0,
        punts=puntuacio.visual_punts,
    )


def _afegeig_aportacioresposta(
        preguntadinstipusespai: PreguntaDinsTipusEspai,
        codi_pregunta,
        percentatge_aportacio):

    # Si aquella pregunta no té aportacio no fem res
    if not percentatge_aportacio:
        return

    # Busquem la resposta
    resposta = (
        preguntadinstipusespai
        .pregunta
        .resposta_set
        .filter(codi__startswith=codi_pregunta+"-")
        [0]
    )

    # Insertem
    AportacioResposta.objects.create(
        preguntadinstipusespai=preguntadinstipusespai,
        resposta=resposta,
        percentatge_aportacio=percentatge_aportacio
    )


def __get_disc(pk): return Discapacitat.objects.get(pk=pk)
