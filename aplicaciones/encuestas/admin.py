from django.contrib import admin
from aplicaciones.encuestas.models import Preguntas, Eleccion
# Register your models here.
admin.site.register(Preguntas)
admin.site.register(Eleccion)