from typing import Dict
from pydantic import BaseModel


class Traductor(BaseModel):
    traduccions: Dict[str, Dict[str, str]] = {}

    def tradueix(self, lang: str, codi: str) -> str:
        return self.traduccions[lang][codi]
