from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.shortcuts import redirect
from django.urls import reverse
from django_tables2 import SingleTableView
from django.views.generic.edit import CreateView
from espais.tables import EspaiTable
from .models import Espai


class EspaiListView(SingleTableView):
    model = Espai
    table_class = EspaiTable
    template_name = 'espais/llista.html'


class EspaiCreateView(CreateView):
    model = Espai
    fields = ['nom', 'municipi', 'adreca', 'tipus', ]
    template_name = 'cform.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(
            Submit('submit', 'Create', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse("espais:espais__blank__blank")