import factory
from decimal import Decimal
from django.utils.text import Truncator
from django.core.validators import MinValueValidator, MaxValueValidator
from math import isclose
from .models import (
    AgrupacioPreguntes,
    Pregunta,
    Resposta,
    PreguntaDinsTipusEspai,
    PuntuacioMaxima,
    AportacioResposta
)
from espais.factories import TipusEspaiFactory
from accessibilitats.factories import DiscapacitatFactory


class AgrupacioPreguntesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AgrupacioPreguntes

    tipusespai = factory.SubFactory(TipusEspaiFactory)
    order = factory.Sequence(lambda n: n)
    text_ca = factory.Faker('sentence', nb_words=6)
    text_es = factory.Faker('sentence', nb_words=6)
    text_en = factory.Faker('sentence', nb_words=6)


class PreguntaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pregunta

    text_ca = factory.Faker('sentence', nb_words=6)
    text_es = factory.Faker('sentence', nb_words=6)
    text_en = factory.Faker('sentence', nb_words=6)
    help_text_ca = factory.Faker('sentence', nb_words=6)
    help_text_es = factory.Faker('sentence', nb_words=6)
    help_text_en = factory.Faker('sentence', nb_words=6)


class RespostaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Resposta

    text_ca = factory.Faker('sentence', nb_words=6)
    text_es = factory.Faker('sentence', nb_words=6)
    text_en = factory.Faker('sentence', nb_words=6)


class PreguntaDinsTipusEspaiFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PreguntaDinsTipusEspai

    agrupaciopreguntes = factory.SubFactory(AgrupacioPreguntesFactory)
    tipusespai_cache = factory.SelfAttribute('agrupaciopreguntes.tipusespai')
    pregunta = factory.SubFactory(PreguntaFactory)
    order = factory.Sequence(lambda n: n)

    @factory.lazy_attribute
    def importancia(self):
        return PreguntaDinsTipusEspai.Importancia.MITJA


class PuntuacioMaximaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PuntuacioMaxima

    preguntadinstipusespai = factory.SubFactory(PreguntaDinsTipusEspaiFactory)
    tipusespai_cache = factory.SelfAttribute('preguntadinstipusespai.tipusespai_cache')
    discapacitat = factory.SubFactory(DiscapacitatFactory)
    afectacio = factory.Faker('pydecimal', right_digits=2, min_value=0, max_value=1)
    afectacio_x_importancia = 0
    punts_sense_arrodonir = 0
    punts = 0


class AportacioRespostaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AportacioResposta

    preguntadinstipusespai = factory.SubFactory(PreguntaDinsTipusEspaiFactory)
    resposta = factory.SubFactory(RespostaFactory)
    percentatge_aportacio = factory.Faker('pydecimal', right_digits=1, min_value=0.1, max_value=1.0)
