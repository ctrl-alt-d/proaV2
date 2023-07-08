import factory
from QandA.models import Discapacitat


class DiscapacitatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Discapacitat

    text_ca = factory.Faker('word')
    text_es = factory.Faker('word')
    text_en = factory.Faker('word')
