from django.urls import path
from espais.views import (
    EspaiListView,
)

urlpatterns = [
    path(r'llista/',
         EspaiListView.as_view(),
         name="espais__blank__blank"),
]
