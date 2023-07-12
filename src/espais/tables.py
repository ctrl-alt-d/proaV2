import django_tables2 as tables
from .models import Espai


class EspaiTable(tables.Table):
    class Meta:
        model = Espai
        fields = ("nom", "tipus")
