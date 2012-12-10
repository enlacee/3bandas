#
from jugador.models import Jugador
from jugador.models import CategoriaJuego
from django.contrib import admin
admin.site.register(CategoriaJuego)
# Error en aparecer como administrable en vistas
#admin.site.register(Jugador)