import uuid
from django.db import models
from .profisssional import Profissional
from .paciente import Paciente 



class Consulta(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_consulta = models.DateTimeField(blank=False, null=False, )
    consulta_profissional = models.OneToOneField(Profissional, on_delete=models.CASCADE, blank=False, null=False, related_name='consulta_profissional')
    consulta_paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, blank=False, null=False, related_name='consulta_paciente')
    status_confirmacao = models.BooleanField(default=False, )

    def __str__(self):
        return f"Data da Consulta: {self.data_consulta}   Paciente: {self.consulta_paciente.nome} Profissional: {self.consulta_profissional.nome} Confirmada: {self.confirmacao}"


