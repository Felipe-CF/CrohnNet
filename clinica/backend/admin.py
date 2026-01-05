from django.contrib import admin

from .models.paciente import Paciente
from .models.consulta import Consulta
from .models.profisssional import Profissional
from .models.especialidade import Especialidade
from .models.usuario import Usuario

admin.site.register(Paciente)
admin.site.register(Profissional)
admin.site.register(Consulta)
admin.site.register(Especialidade)
admin.site.register(Usuario)