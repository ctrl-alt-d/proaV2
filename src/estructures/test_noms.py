from estructures.constants import (
    DiscapacitatsEnum, IdiomesEnum, AccessibilitatEnum
)
from estructures.cadenes import ACCESSIBILITATS, DISCAPACITATS, IDIOMES


def test_discapacitats_traduccions():

    assert DISCAPACITATS.tradueix(
        IdiomesEnum.CATALA,
        DiscapacitatsEnum.VISUAL) == "Visual"

    for idioma in IdiomesEnum:
        for x in DiscapacitatsEnum:
            assert DISCAPACITATS.tradueix(idioma, x)


def test_idiomes_traduccions():

    assert IDIOMES.tradueix(
        IdiomesEnum.CATALA,
        IdiomesEnum.CATALA) == "Català"

    for idioma in IdiomesEnum:
        for x in IdiomesEnum:
            assert IDIOMES.tradueix(idioma, x)


def test_accessibilitats_traduccions():

    assert ACCESSIBILITATS.tradueix(
        IdiomesEnum.CATALA,
        AccessibilitatEnum.ACCESSIBLE) == "Accessible"

    for idioma in IdiomesEnum:
        for x in AccessibilitatEnum:
            assert ACCESSIBILITATS.tradueix(idioma, x)
