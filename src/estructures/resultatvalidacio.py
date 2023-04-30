from typing import List, Optional, Dict
from pydantic import BaseModel
from estructures.constants import (
    IdiomesEnum, DiscapacitatsEnum, AccessibilitatEnum
)


class QA(BaseModel):
    pregunta_display: str
    pregunta_codi: str
    resposta_display: Optional[str]
    resposta_codi: Optional[str]
    categoria_display: str
    categoria_codi: str
    punts_obtinguts: str
    punts_possibles: str
    punts_diferencia: float


class ResultatDiscapacitat(BaseModel):
    discapacitat_codi: DiscapacitatsEnum
    discapacitat_display: str
    assoliment_codi: AccessibilitatEnum
    assoliment_display: str
    respostes: List[QA]
    penalitzen: List[QA]
    exclouen: List[QA]
    punts_obtinguts: float
    punts_possibles: float
    punts_diferencia: float
    percentatge_assoliment: float


ResultatPerDiscapacitat = List[ResultatDiscapacitat]
ResultatPerIdioma = Dict[IdiomesEnum, ResultatPerDiscapacitat]


class Resultats(BaseModel):
    """
    Aquesta data class serveix per guardar els resultats del
    càlcul de l'accessibilitat d'un espai en un camp json
    del model HistoricAccessibilitatEspai
    """
    resultatPerIdioma: ResultatPerIdioma
