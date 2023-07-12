from django.shortcuts import render

from django_tables2 import SingleTableView

from espais.tables import EspaiTable
from .models import Espai


class EspaiListView(SingleTableView):
    model = Espai
    table_class = EspaiTable
    template_name = 'espais/llista.html'
