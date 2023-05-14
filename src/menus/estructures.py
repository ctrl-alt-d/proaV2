from pydantic import BaseModel
from typing import List


class MenuItem(BaseModel):
    text: str
    visible: bool
    viewprefix: str
    viewdefault: str
    submenus: List['MenuItem'] = []


class MenuPrintItem(BaseModel):
    text: str
    actiu: bool
    url: str


class MenuPrint(BaseModel):
    activarmenuusuari: bool
    primernivell: List[MenuPrintItem] = []
    segonnivell: List[MenuPrintItem] = []
    tercernivell: List[MenuPrintItem] = []
