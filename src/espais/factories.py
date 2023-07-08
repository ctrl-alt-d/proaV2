import factory
from QandA.models import TipusEspai


class TipusEspaiFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TipusEspai

    text_ca = factory.Faker('sentence', nb_words=4)
    text_es = factory.Faker('sentence', nb_words=4)
    text_en = factory.Faker('sentence', nb_words=4)
