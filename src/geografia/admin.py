from django.contrib import admin
from .models import Provincia, Comarca, Municipi

# Register your models here.

class ProvinciaAdmin(admin.ModelAdmin):
    model = Provincia    

admin.site.register(Provincia, ProvinciaAdmin)

class ComarcaAdmin(admin.ModelAdmin):
    model = Comarca    

admin.site.register(Comarca, ComarcaAdmin)

class MunicipiAdmin(admin.ModelAdmin):
    model = Comarca    

admin.site.register(Municipi, MunicipiAdmin)




