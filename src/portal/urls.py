from django.urls import path
from portal.views import (enquesta,
                          )

urlpatterns = [
    path(r'enquesta/',
         enquesta,
         name="enquesta__blank__blank"),
]
