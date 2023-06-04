from django.contrib import admin
from QandA.models import AgrupacioPreguntes, PreguntaDinsTipusEspai
from .models import (
    P_Pregunta_i_Respostes, P_TipusEspai_AgrupacionsP, P_TipusEspai_Preguntes
)

from QandA.models import Resposta


class RespostaInline(admin.TabularInline):
    fields = ["text_ca", "imatge"]
    model = Resposta
    extra = 0

class PreguntaAdmin(admin.ModelAdmin):
    ordering = ["text_ca"]
    search_fields = ["text_ca", "text_es", "text_en"]
    fields = ["text_ca", "help_text_ca", "imatge"]
    inlines = [
        RespostaInline,
    ]


admin.site.register(P_Pregunta_i_Respostes, PreguntaAdmin)


# Manteniment de les Agrupacions de Preguntes de cada Tipus d'espai


class AgrupacioPreguntesInline(admin.TabularInline):
    fields = ["order", "text_ca"]
    model = AgrupacioPreguntes
    extra = 0


class TipusEspaiAdmin(admin.ModelAdmin):
    fields = ["text_ca"]
    inlines = [
        AgrupacioPreguntesInline,
    ]


admin.site.register(P_TipusEspai_AgrupacionsP, TipusEspaiAdmin)


# Manteniment de les Preguntes de cada Tipus d'espai


class PreguntaDinsTipusEspaiInline(admin.StackedInline):
    model = PreguntaDinsTipusEspai
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


class TipusEspaiAdmin(admin.ModelAdmin):
    fields = ["text_ca"]
    inlines = [
        PreguntaDinsTipusEspaiInline,
    ]


admin.site.register(P_TipusEspai_Preguntes, TipusEspaiAdmin)
