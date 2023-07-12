from django.shortcuts import render, redirect
from estructures.constants import TipusEspaiEnum
from formularis.crispyhelpers import PreguntaFormHelper
from formularis.forms import PreguntaForm

from espais.models import TipusEspai
from demoandtest.createDemoData import run as creaDemoData
from django.contrib.auth.decorators import login_required
from django.conf import settings


def home(request):
    if request.user.is_authenticated:
        return redirect("espais:espais__llista__blank")
    else:
        return redirect(settings.LOGIN_URL)


@login_required
def enquesta(request):
    """
    Prova de concepte per tal de carregar les preguntes dinàmicament des de la base de dades
    """
    # Prova de concepte. Cal fer un formulari dimàmica amb les preguntes i possibles respostes

    preguntaform = PreguntaForm()

    hut = TipusEspai.objects.get(codi=TipusEspaiEnum.HUT)

    preguntes = [
        preguntadinstipusespai.pregunta
        for agrupacio
        in hut.agrupaciopreguntes_set.all()
        for preguntadinstipusespai
        in agrupacio.preguntadinstipusespai_set.all()]

    for pregunta in preguntes:
        respostes = pregunta.resposta_set.values_list('codi', 'text_ca')
        preguntaform.afegir_pregunta(
            fieldname=pregunta.codi,
            label=pregunta.text_ca,
            respostes=respostes, )

    preguntaform.helper = PreguntaFormHelper(hut)

    ctx = {
        'form': preguntaform,
    }

    return render(request, "portal/home.html", ctx)
