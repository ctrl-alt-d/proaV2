from typing import List
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, Submit
)
from QandA.models import AgrupacioPreguntes

from espais.models import TipusEspai


def _calcula_camps(agrupacio: AgrupacioPreguntes) -> List[str]:
    return [
        preguntadinstipusespai.pregunta.codi
        for preguntadinstipusespai
        in agrupacio.preguntadinstipusespai_set.all()
    ]


def _calcula_layout(agrupacio: AgrupacioPreguntes) -> Fieldset:
    camps = _calcula_camps(agrupacio)
    return Fieldset(
        agrupacio.text_ca,
        *camps,
    )


class PreguntaFormHelper(FormHelper):
    """
    Layout for pregunta formset
    """

    def __init__(self, tipusespai: TipusEspai, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'

        fieldsets = [
            _calcula_layout(agrupacio)
            for agrupacio in tipusespai.agrupaciopreguntes_set.all()
        ]

        self.layout = Layout(
            *fieldsets,
            Submit('submit', 'Submit', css_class='button white'),
        )
        self.render_required_fields = True
