from estructures.cadenes import ACCESSIBILITATS, DISCAPACITATS
from estructures.resultatvalidacio import (
    QA, ResultatDiscapacitat, Resultats
)
from estructures.constants import (
    IdiomesEnum, DiscapacitatsEnum, AccessibilitatEnum
)
import json


def test_estructura_exemple():
    """
    Disposar d'una estructura auto-continguda on emmagatzemar els resultats de
    la validació d'un espai és crític.

    Aquest test serveix per documentar i provar com s'informa aquesta
    estructura i com després s'accedeix a les dades.

    És important destacar que la UI ha de tenir fàcil poder navegar pels
    camps d'aquesta estructura per poder pintar amb facilitat els resultats
    d'una validació.

    Aquesta estructura és autocontinguda perquè pot passar que es canviin
    preguntes, pesos, respostes, etc a la base de dades. Llavors, si només
    emmagatzemessin claus forànes a aquestes estructures, ens podríem trobar
    que les estructures han canviat i la validacó de l'espai ha quedat
    obsoleta i s'ha perdut el seu contingut.

    Nota: pot ser que aquesta estructura, durant el desenvolupament, es
    modifiqui per posar-hi més dades. Cal mantenir aquest test
    sempre actualitzat per garantir que l'estructura és correcte.

    Nota: hi ha dades que no apareixeran en aquest json sino que seran camps
    del model HistoricAccessibilitatEspai, com per exemple les dates, si
    es tracta d'una validació o proposta d'usuari, etc. El json només conté
    els resultats dels càlculs d'accessibilitat sobre l'espai.

    Nota: si l'estructura es modifiqués un cop el sistema ha passat a producció
    caldria guardar versions de l'estructura per saber sobre quines classes
    deserialitzar-la.
    """

    # exemple de construir resultats d'una enquesta sobre espai
    # en aquest exemple ens inventem les dades, però les dades
    # haurian de sortir dels models de preguntes, respostes i
    # parametritzacions de càlculs
    resultat = _calcula_resultats()

    # test els resultats s'han creat
    assert resultat

    # test es pot serialitzar i deserialitzar el resultat
    # recordem que s'emmagatzemarà en un camp json de la base
    # de dades
    resultat_json = resultat.json()
    resultat_from_json = Resultats.parse_raw(resultat_json)

    # exemple d'agafar tots els resultats en català:
    resultat_cat = resultat_from_json.resultatPerIdioma[IdiomesEnum.CATALA]

    # exemple d'agafar el resultats de discapacitata visual:
    resultat_discapacitat_visual = next(
        x for x in resultat_cat
        if x.discapacitat_codi == DiscapacitatsEnum.VISUAL)
    
    # exemple d'agafar l'assoliment d'aquesta discapacitat:
    assoliment_visual = resultat_discapacitat_visual.assoliment_codi
    assert assoliment_visual == AccessibilitatEnum.ACCESSIBLE

    # exemple d'agafar la primera pregunta-resposta dels resultats de visual:
    primera_resposta_visual = resultat_discapacitat_visual.respostes[0]
    expected_q_cat = "Hi ha porta giratòria?"
    assert primera_resposta_visual.pregunta_display == expected_q_cat

    # mostrar, en maco, el json de com s'emmagatzemen les dades:
    # per veure'l fer servir: `pytest -s`
    print(json.dumps(resultat.dict(), indent=2))


def _calcula_resultats():
    resultats = {
        idioma: _calcula_resultat(idioma)
        for idioma in IdiomesEnum
    }
    return Resultats(
        resultatPerIdioma=resultats
    )


def _calcula_resultat(idioma):
    assoliment_display = ACCESSIBILITATS.tradueix(
        idioma, AccessibilitatEnum.ACCESSIBLE)

    def discapacitat_display(discapacitat):
        return DISCAPACITATS.tradueix(idioma, discapacitat)

    return [
        ResultatDiscapacitat(
            discapacitat_codi=discapacitat,
            discapacitat_display=discapacitat_display(discapacitat),
            assoliment_codi=AccessibilitatEnum.ACCESSIBLE,
            assoliment_display=assoliment_display,
            respostes=[_calcula_qa(idioma)],
            penalitzen=[],
            exclouen=[],
            punts_obtinguts=10,
            punts_possibles=20,
            punts_diferencia=0.5,
            percentatge_assoliment=50.0
        )
        for discapacitat in DiscapacitatsEnum
    ]


def _calcula_qa(idioma):
    pregunta = {
        IdiomesEnum.CATALA: "Hi ha porta giratòria?",
        IdiomesEnum.CASTELLA: "Hay puerta giratoria?",
        IdiomesEnum.ANGLES: "Is there a revolving door?"
    }
    resposta = {
        IdiomesEnum.CATALA: "Sí",
        IdiomesEnum.CASTELLA: "Si",
        IdiomesEnum.ANGLES: "Yes"
    }
    categoria = {
        IdiomesEnum.CATALA: "Accés a l'espai",
        IdiomesEnum.CASTELLA: "Aceso al espaci",
        IdiomesEnum.ANGLES: "Access to space"
    }
    qa = QA(
        pregunta_display=pregunta[idioma],
        pregunta_codi="porta-giratoria",
        resposta_display=resposta[idioma],
        resposta_codi="si",
        categoria_display=categoria[idioma],
        categoria_codi="acces",
        punts_obtinguts="5",
        punts_possibles="10",
        punts_diferencia=0.5
    )
    return qa
