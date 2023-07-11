from typing import List
from pydantic import BaseModel

from estructures.constants import DiscapacitatsEnum


class ExclusioStruct(BaseModel):
    codi: str
    discapacitat: str
    resposta: str


AI = {
    ("f_02_003", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}
AL = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
AO = {
    ("f_02_003", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}
AP = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_11_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}
BA = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_02_004", DiscapacitatsEnum.CADIRADERODES, "no",),
}
CA = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
CH = {
}
CO = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
ER = {
    ("f_02_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
HO = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_13_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}
HU = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_11_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}
IT = {
}
MU = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
OT = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
PC = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
RE = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
}
RU = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_03_003", DiscapacitatsEnum.CADIRADERODES, "no",),
    ("f_12_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}
TA = {
    ("f_03_001", DiscapacitatsEnum.CADIRADERODES, "no",),
}


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


def ExclusioStructFactoria(
    codi: str,
    discapacitat: str,
    resposta: str,
):
    return ExclusioStruct(
        codi=codi,
        discapacitat=discapacitat,
        resposta=resposta)


def f(d) -> List[ExclusioStruct]:
    return [ExclusioStructFactoria(*x) for x in d]


Exclusions = dict([
    (MUSEU, f(MU)),
    (RESTAURANT, f(RE)),
    (ALLOTJAMENT_RURAL, f(RU)),
    (APARTAMENT, f(AP)),
    (HUT, f(HU)),
    (HOTEL, f(HO)),
    (CAMPING, f(CA)),
    (ALBERG, f(AL)),
    (ZONA_BANY, f(BA)),
    (ACTIVITAT_INDOOR, f(AI)),
    (ACTIVITAT_OUTDOOR, f(AO)),
    (COMERC, f(CO)),
    (OFICINA_DE_TURISME, f(OT)),
    (ITINERARI, f(IT)),
    (CENTRE_HISTORIC, f(CH)),
    (PATRIMONI_CULTURAL, f(PC)),
    (ESPAI_REUNIO, f(ER)),
    (TAXI, f(TA)),
])
