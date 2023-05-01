from django import forms


class PreguntaFormBackup(forms.Form):
    def __init__(self, label, respostes, *args, **kwargs):

        super(PreguntaForm, self).__init__(*args, **kwargs)

        widget = forms.RadioSelect(choices=respostes)
        self.fields['respostes'].widget = widget
        self.fields['respostes'].label = label

    respostes = forms.ChoiceField()


class PreguntaForm(forms.Form):
    """
    Permet afegir preguntes dinamicament
    """

    def afegir_pregunta(self, fieldname, label, respostes):
        """
        permet afegir una pregunta
        """
        widget = forms.RadioSelect(choices=respostes)
        field = forms.ChoiceField(widget=widget, label=label)
        self.fields[fieldname] = field
        self.fields[fieldname].widget = widget
        self.fields[fieldname].label = label
