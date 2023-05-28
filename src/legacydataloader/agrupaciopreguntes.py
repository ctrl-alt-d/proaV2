from QandA.models import AgrupacioPreguntes
from espais.models import TipusEspai
from legacydata.tipusespais import GetTipusEspaisStructs
from legacydataloader.tipus import importtipus


def importagrupaciopreguntes():
    # Esborrar els que ja hi són
    codis = [x.codi for x in GetTipusEspaisStructs()]
    _ = (
        AgrupacioPreguntes
        .objects
        .filter(tipusespai__codi__in=codis)
        .delete()
    )

    # Importar els tipus
    importtipus()

    # Importar agrupacions
    for tipus_legacy in GetTipusEspaisStructs():
        afegits = []
        tipus_bd = TipusEspai.objects.get(pk=tipus_legacy.codi)
        categories = [
            (k, v)
            for k, v in tipus_legacy.preguntes.items()
            if k.lower().startswith("ct_")
        ]
        for categoria in categories:
            codi = categoria[0].split("_")[1]
            nom = categoria[1]
            item = AgrupacioPreguntes.objects.create(
                codi=tipus_bd.codi + "-" + codi,
                tipusespai=tipus_bd,
                text_ca=nom
            )
            afegits.append(item)

        tipus_bd.set_agrupaciopreguntes_order(afegits)
