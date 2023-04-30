from enum import StrEnum


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
