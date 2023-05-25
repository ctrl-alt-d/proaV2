from django.contrib import admin

from django.contrib import admin
from .models import Provincia, Comarca, Municipi

# Register your models here.
admin.site.register(Provincia, Comarca, Municipi)


