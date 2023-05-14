from django.shortcuts import render
from formularis.crispyhelpers import PreguntaFormHelper
from formularis.forms import PreguntaForm

from formularis.models import Pregunta
from demoandtest.createDemoData import run as creaDemoData
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """
    Prova de concepte per tal de carregar les preguntes dinàmicament des de la base de dades
    """

    creaDemoData()
    # Prova de concepte. Cal fer un formulari dimàmica amb les preguntes i possibles respostes

    preguntaform = PreguntaForm()

    preguntes = Pregunta.objects.all()
    for pregunta in preguntes:
        respostes = pregunta.respostes.values_list('id', 'text')
        preguntaform.afegir_pregunta(
            fieldname=f"p-{str(pregunta.id)}",
            label=pregunta.text,
            respostes=respostes, )

    fieldnames = [f"p-{str(pregunta.id)}" for pregunta in preguntes]

    preguntaform.helper = PreguntaFormHelper(fieldnames)

    ctx = {
        'form': preguntaform,
    }

    return render(request, "portal/home.html", ctx)
