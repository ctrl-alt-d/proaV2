from django.test import TestCase

from QandA.factories import PreguntaDinsTipusEspaiFactory, PuntuacioMaximaFactory
from QandA.models import PuntuacioMaxima
from accessibilitats.factories import DiscapacitatFactory
from django.db.models import Sum, Count
from QandA.helpers import recalculapunts


class EsReparteixenElsPuntsTest(TestCase):

    def recalcula_punts_funciona_be(self):

        # Arrange
        discapacitat = DiscapacitatFactory.create()
        preguntadinstipusespai = PreguntaDinsTipusEspaiFactory.create()
        tipusespai = preguntadinstipusespai.agrupaciopreguntes.tipusespai

        PuntuacioMaximaFactory.create_batch(100)  # 100 valors random

        for _ in range(50):  # 50 valors del nostre espai i discapacitat
            punts = PuntuacioMaximaFactory(
                preguntadinstipusespai=preguntadinstipusespai,
                discapacitat=discapacitat)
            punts.save()

        assert len(PuntuacioMaxima.objects.all()) == 150

        punts, recompte = self._calcula_agregats(discapacitat, tipusespai)
        assert recompte == 50, f"recompte is {recompte}, but it should be 50"
        assert punts == 0, f"punts is {punts}, but it should be 0"

        # Act
        recalculapunts.recalcula(discapacitat, tipusespai)

        # Assert
        punts, recompte = self._calcula_agregats(discapacitat, tipusespai)
        assert recompte == 50, f"recompte is {recompte}, but it should be 50"
        assert punts == 100, f"punts is {punts}, but it should be 100"

    def _calcula_agregats(self, discapacitat, tipusespai):
        agregats = (
            PuntuacioMaxima
            .objects
            .filter(
                tipusespai_cache=tipusespai,
                discapacitat=discapacitat
            )
            .aggregate(total=Sum("punts"), recompte=Count("*"))
        )

        punts = agregats["total"]
        recompte = agregats["recompte"]
        return punts, recompte
