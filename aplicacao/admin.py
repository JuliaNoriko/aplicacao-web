from django.contrib import admin
from .models import PacienteHasMedico, PacienteHasLeito
from .models import Paciente, Medico, Leito, Hospital 

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Hospital)
admin.site.register(Leito)

admin.site.register(PacienteHasMedico)
admin.site.register(PacienteHasLeito)
