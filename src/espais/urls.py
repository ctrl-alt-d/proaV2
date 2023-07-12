from django.urls import path
from espais.views import (
    EspaiCreateView,
    EspaiListView,
)

urlpatterns = [
    path(r'llista/',
         EspaiListView.as_view(),
         name="espais__blank__blank"),
    path(r'nou/',
         EspaiCreateView.as_view(),
         name="espais__create__blank"),
]
