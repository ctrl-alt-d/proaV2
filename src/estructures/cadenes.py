
from estructures.constants import (
    DiscapacitatsEnum, IdiomesEnum, AccessibilitatEnum
)
from estructures.helpers import Traductor


_discapacitats = {
    IdiomesEnum.CATALA: {
        DiscapacitatsEnum.AUDITIU: "Auditiu",
        DiscapacitatsEnum.CADIRADERODES: "Cadira de rodes",
        DiscapacitatsEnum.FAMILIAR: "Familiar",
        DiscapacitatsEnum.MOBILITATREDUIDA: "Mobilitat reduida",
        DiscapacitatsEnum.VISUAL: "Visual",
    },
    IdiomesEnum.CASTELLA: {
        DiscapacitatsEnum.AUDITIU: "Auditivo",
        DiscapacitatsEnum.CADIRADERODES: "Silla de ruedas",
        DiscapacitatsEnum.FAMILIAR: "Familiar",
        DiscapacitatsEnum.MOBILITATREDUIDA: "Movilidad reducida",
        DiscapacitatsEnum.VISUAL: "Visual",
    },
    IdiomesEnum.ANGLES: {
        DiscapacitatsEnum.AUDITIU: "Hearing impaired",
        DiscapacitatsEnum.CADIRADERODES: "Wheelchair user",
        DiscapacitatsEnum.FAMILIAR: "Family member",
        DiscapacitatsEnum.MOBILITATREDUIDA: "Reduced mobility",
        DiscapacitatsEnum.VISUAL: "Visually impaired",
    },
}

_idiomes = {
    IdiomesEnum.CATALA: {
        IdiomesEnum.CATALA: "Català",
        IdiomesEnum.CASTELLA: "Castellà",
        IdiomesEnum.ANGLES: "Anglès",
    },
    IdiomesEnum.CASTELLA: {
        IdiomesEnum.CATALA: "Catalán",
        IdiomesEnum.CASTELLA: "Castellano",
        IdiomesEnum.ANGLES: "Inglés",
    },
    IdiomesEnum.ANGLES: {
        IdiomesEnum.CATALA: "Catalan",
        IdiomesEnum.CASTELLA: "Spanish",
        IdiomesEnum.ANGLES: "English",
    },
}

_accessibilitats = {
    IdiomesEnum.CATALA: {
        AccessibilitatEnum.ACCESSIBLE: "Accessible",
        AccessibilitatEnum.UTILITZABLE: "Utilitzable",
        AccessibilitatEnum.NOPRACTICABLE: "No practicable",
    },
    IdiomesEnum.CASTELLA: {
        AccessibilitatEnum.ACCESSIBLE: "Accesible",
        AccessibilitatEnum.UTILITZABLE: "Utilizable",
        AccessibilitatEnum.NOPRACTICABLE: "No practicable",
    },
    IdiomesEnum.ANGLES: {
        AccessibilitatEnum.ACCESSIBLE: "Accessible",
        AccessibilitatEnum.UTILITZABLE: "Usable",
        AccessibilitatEnum.NOPRACTICABLE: "Not practicable",
    },
}


DISCAPACITATS = Traductor(traduccions=_discapacitats)
IDIOMES = Traductor(traduccions=_idiomes)
ACCESSIBILITATS = Traductor(traduccions=_accessibilitats)
