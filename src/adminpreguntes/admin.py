from django import forms
from django.contrib import admin
from QandA.models import AgrupacioPreguntes, Pregunta, PreguntaDinsTipusEspai, PuntuacioMaxima
from accessibilitats.models import Discapacitat
from estructures.constants import DiscapacitatsEnum
from .models import (
    P_Pregunta_i_Respostes, P_TipusEspai_AgrupacionsP, P_TipusEspai_Preguntes, P_TipusEspai_PuntuacionsMaximes_Visual
)

from QandA.models import Resposta
from django.contrib.admin.widgets import AutocompleteSelect
from QandA.helpers import recalculapunts

#
# Preguntes i respostes
#


class RespostaInline(admin.TabularInline):
    fields = ["text_ca", "imatge"]
    model = Resposta
    extra = 0


class PreguntaAdmin(admin.ModelAdmin):
    ordering = ["text_ca"]
    list_filter = [
        "agrupaciopreguntes__tipusespai__text_ca",
    ]
    search_fields = ["text_ca", "text_es", "text_en"]
    fields = ["text_ca", "help_text_ca", "imatge"]
    inlines = [
        RespostaInline,
    ]


admin.site.register(P_Pregunta_i_Respostes, PreguntaAdmin)


#
# Agrupacions de Preguntes a cada Tipus d'espai
#


class AgrupacioPreguntesInline(admin.TabularInline):
    fields = ["order", "text_ca"]
    model = AgrupacioPreguntes
    extra = 0


class AgrupacioPreguntesTipusEspaiAdmin(admin.ModelAdmin):
    fields = ["text_ca"]
    inlines = [
        AgrupacioPreguntesInline,
    ]


admin.site.register(
    P_TipusEspai_AgrupacionsP, AgrupacioPreguntesTipusEspaiAdmin)


#
# Preguntes de cada Tipus d'espai
#
@admin.register(Pregunta)
class WorkerModelAdmin(admin.ModelAdmin):
    search_fields = ['text_ca']


class PreguntaDinsTipusEspaiForm(forms.ModelForm):
    class Meta:
        widgets = {
            'pregunta': AutocompleteSelect(
                PreguntaDinsTipusEspai._meta.get_field('pregunta'),
                admin.site,
                attrs={'style': 'width:calc(100% - 60px);'}
            ),
        }


class PreguntaDinsTipusEspaiInline(admin.StackedInline):
    model = PreguntaDinsTipusEspai
    form = PreguntaDinsTipusEspaiForm
    autocomplete_fields = ['pregunta']
    extra = 0
    ordering = [
        "tipusespai_cache__text_ca",
        "agrupaciopreguntes__order",
        "order"]

    def get_formset(self, request, obj=None, **kwargs):
        self.parent_obj = obj
        return super().get_formset(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Cal restringir: només les agrupacions d'aquell tipus d'espai
        """
        if db_field.name == "agrupaciopreguntes":
            kwargs["queryset"] = (
                AgrupacioPreguntes
                .objects
                .filter(tipusespai=self.parent_obj)
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PreguntaTipusEspaiAdmin(admin.ModelAdmin):
    fields = ["text_ca"]
    inlines = [
        PreguntaDinsTipusEspaiInline,
    ]


admin.site.register(P_TipusEspai_Preguntes, PreguntaTipusEspaiAdmin)


#
# Puntuacions Màximes Visual
#


class PuntuacioMaximaVisualDinsTipusEspaiInline(admin.TabularInline):

    model = PuntuacioMaxima
    readonly_fields = [
        'preguntadinstipusespai',
        'afectacio_x_importancia',
        'punts_sense_arrodonir',
    ]
    fields = [
        'preguntadinstipusespai',
        'afectacio',
        'afectacio_x_importancia',
        'punts_sense_arrodonir',
        'punts'
    ]
    extra = 0

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(discapacitat=DiscapacitatsEnum.VISUAL)

    def get_formset(self, request, obj=None, **kwargs):
        self.parent_obj = obj
        return super().get_formset(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Cal restringir: només les preguntes d'aquell tipus d'espai
                        i discapacitat
        """
        if db_field.name == "preguntadinstipusespai":
            kwargs["queryset"] = (
                PreguntaDinsTipusEspai
                .objects
                .filter(agrupaciopreguntes__tipusespai=self.parent_obj)
            )
        if db_field.name == "discapacitat":
            kwargs["queryset"] = _get_discapacitat_by_code(
                DiscapacitatsEnum.VISUAL)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.action(description="Recalcula punts")
def recalcula_punts_visual(modeladmin, request, queryset):
    discapacitat = _get_discapacitat_by_code(DiscapacitatsEnum.VISUAL).first()
    for tipusespai in list(queryset.all()):
        print(str(tipusespai))
        recalculapunts.recalcula(discapacitat, tipusespai)


class PuntuacioMaximaVisualTipusEspaiAdmin(admin.ModelAdmin):
    fields = ["text_ca"]
    inlines = [
        PuntuacioMaximaVisualDinsTipusEspaiInline,
    ]
    actions = [recalcula_punts_visual]


admin.site.register(
    P_TipusEspai_PuntuacionsMaximes_Visual,
    PuntuacioMaximaVisualTipusEspaiAdmin)


def _get_discapacitat_by_code(codi):
    return (
        Discapacitat
        .objects
        .filter(codi=codi)
    )
