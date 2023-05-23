from django.contrib import admin

from django.contrib import admin
from .models import Provincia, ConsellComarcal, Municipi

# Register your models here.
admin.site.register(Provincia, ConsellComarcal, Municipi)


