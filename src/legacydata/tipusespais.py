from pydantic import BaseModel

from legacydata.questions import (
    AI, AL, AO, AP, BA, CA, CH, CO, ER, HO, HU, IT, MU, OT, PC, RE, RU, TA
)

MUSEU = "MU"
RESTAURANT = "RE"
ALLOTJAMENT_RURAL = "RU"
APARTAMENT = "AP"
HUT = "HU"
HOTEL = "HO"
CAMPING = "CA"
ALBERG = "AL"
ZONA_BANY = "BA"
ACTIVITAT_INDOOR = "AI"
ACTIVITAT_OUTDOOR = "AO"
COMERC = "CO"
OFICINA_DE_TURISME = "OT"
ITINERARI = "IT"
CENTRE_HISTORIC = "CH"
PATRIMONI_CULTURAL = "PC"
ESPAI_REUNIO = "ER"
TAXI = "TA"

TipusEspaisList = (
    (MUSEU, ("Museu / Centre d'interpretació", MU)),
    (RESTAURANT, ("Restaurant", RE)),
    (ALLOTJAMENT_RURAL, ("Allotjament rural", RU)),
    (APARTAMENT, ("Apartament", AP)),
    (HUT, ("HUT", HU)),
    (HOTEL, ("Hotel", HO)),
    (CAMPING, ("Càmping", CA)),
    (ALBERG, ("Alberg-Casa de Colònies", AL)),
    (ZONA_BANY, ("Zona de bany", BA)),
    (ACTIVITAT_INDOOR, ("Activitat indoor", AI)),
    (ACTIVITAT_OUTDOOR, ("Activitat outdoor", AO)),
    (COMERC, ("Comerç", CO)),
    (OFICINA_DE_TURISME, ("Oficina de turisme", OT)),
    (ITINERARI, ("Itinerari", IT)),
    (CENTRE_HISTORIC, ("Centre Històric", CH)),
    (PATRIMONI_CULTURAL, ("Patrimoni cultural", PC)),
    (ESPAI_REUNIO, ("Espai de reunions", ER)),
    (TAXI, ("Taxi", TA)),
)


class TipusEspaiStruct(BaseModel):
    codi: str
    text: str
    preguntes: dict


def GetTipusEspaisStructs():
    return [
        TipusEspaiStruct(
            codi=item[0],
            text=item[1][0],
            preguntes=item[1][1])
        for item in TipusEspaisList
    ]

