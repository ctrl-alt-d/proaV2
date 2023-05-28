from espais.models import TipusEspai
from legacydata.tipusespais import GetTipusEspaisStructs


def importtipus():
    # Esborrar els que ja hi són
    codis = [x.codi for x in GetTipusEspaisStructs()]
    TipusEspai.objects.filter(codi__in=codis).delete()

    # Importar
    for tipus in GetTipusEspaisStructs():
        TipusEspai.objects.create(
            codi=tipus.codi,
            text_ca=tipus.text)
