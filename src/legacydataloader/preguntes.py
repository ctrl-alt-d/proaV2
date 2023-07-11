from QandA.helpers.modelhelpers import calculacodi
from QandA.models import Pregunta, Resposta
from legacydata.tipusespais import GetTipusEspaisStructs
from legacydata.respostes import respostesdict


def importpreguntes():
    totes = [
        item[1]
        for x in GetTipusEspaisStructs()
        for item in x.preguntes.items()
        if item[0].startswith("f_")
    ]

    # Importar
    for q in totes:
        text = q[0]
        help_text = q[2]
        localitzador_resposta = q[1]
        pregunta, c = Pregunta.objects.get_or_create(
            text_ca=text,
            defaults={"help_text_ca": help_text})

        if (not c):
            continue

        respostes = respostesdict[localitzador_resposta]

        order = 10
        for resposta in respostes:
            codi = resposta[0] + "-" + calculacodi()
            text = resposta[1]
            Resposta.objects.create(
                pregunta=pregunta,
                codi=codi,
                text_ca=text,
                order=order
            )
            order += 10
