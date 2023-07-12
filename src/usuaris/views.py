from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms.models import modelform_factory
from django.contrib import messages
from usuaris.models import Perfil
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import FormActions


@login_required
def edita_perfil(request):

    perfil = request.user.perfil

    fields = ["nom",
              "cognoms",
              "organitzacio",
              "telefon", ]

    widgets = {
    }

    formF = modelform_factory(Perfil, fields=fields, widgets=widgets)
    if request.method == 'POST':
        form = formF(request.POST, instance=perfil)
        if form.is_valid():
            perfil = form.save(commit=False)

            perfil.save()

            url_next = reverse('home__blank__blank')
            messages.success(request, "Canvis realitzats correctament.")
            return HttpResponseRedirect(url_next)
    else:
        form = formF(instance=perfil)

    form.helper = FormHelper()

    form.helper.layout = Layout(
        Fieldset(
            "Dades Usuari: {u}".format(u=perfil.nom),
            *fields
        ),
        FormActions(
            Submit('save_changes', 'Desar', css_class="btn-dark"),
        )
    )

    return render(request,
                  'cform.html',
                  {
                      'form': form,
                  })
