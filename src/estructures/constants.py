from enum import StrEnum


class TipusEspaiEnum(StrEnum):
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


class DiscapacitatsEnum(StrEnum):
    VISUAL = "visual",
    AUDITIU = "auditiu",
    CADIRADERODES = "cadirarodes",
    MOBILITATREDUIDA = "mobilitatreduida",
    FAMILIAR = "familiar",


class IdiomesEnum(StrEnum):
    CATALA = "cat",
    CASTELLA = "esp",
    ANGLES = "eng",


class AccessibilitatEnum(StrEnum):
    NOPRACTICABLE = "nopracticable"
    UTILITZABLE = "utilitzable"
    ACCESSIBLE = "accessible"
