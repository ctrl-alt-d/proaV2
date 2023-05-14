from django.urls import path
from usuaris.views import (edita_perfil,
                           )

urlpatterns = [
    path(r'edita/',
         edita_perfil,
         name="usuaris__perfil__edita"),
]
