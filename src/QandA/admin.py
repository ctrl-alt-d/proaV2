from django.contrib import admin

from QandA.models import Pregunta, Resposta


class RespostaInline(admin.TabularInline):
    fields = ["text_ca", "imatge"]
    model = Resposta


class PreguntaAdmin(admin.ModelAdmin):
    ordering = ["text_ca"]
    search_fields = ["text_ca", "text_es", "text_en"]    
    fields = ["text_ca", "help_text_ca", "imatge"]
    inlines = [
        RespostaInline,
    ]


admin.site.register(Pregunta, PreguntaAdmin)
