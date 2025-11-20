from django.contrib import admin
from .models import Alumno,Profesor,Materia,ReservaClase

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(ReservaClase)
