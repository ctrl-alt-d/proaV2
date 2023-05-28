from accessibilitats.models import Discapacitat
from estructures.cadenes import DISCAPACITATS
from estructures.constants import DiscapacitatsEnum


def importdiscapacitats():
    for discapacitat in DiscapacitatsEnum:
        Discapacitat.objects.create(
            codi=discapacitat,
            text_ca=DISCAPACITATS.tradueix('cat', discapacitat),
            text_es=DISCAPACITATS.tradueix('esp', discapacitat),
            text_en=DISCAPACITATS.tradueix('eng', discapacitat),
        )
