from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, Submit
)


class PreguntaFormHelper(FormHelper):
    """
    Layout for pregunta formset
    """
    def __init__(self, fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            Fieldset(
                'Prova de concepte',
                *fields,
            ),
            Submit('submit', 'Submit', css_class='button white'),
        )
        self.render_required_fields = True
