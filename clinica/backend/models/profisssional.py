import uuid
from django.db import models
from .especialidade import Especialidade
from backend.models.usuario import Usuario


class Profissional(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.CharField(blank=False, null=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    contato = models.CharField(default='sem telefone', null=False,)
    cpf = models.CharField(max_length=11, blank=False, null=False,)
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, blank=False, null=False, related_name='usuario_pro')
    conselho_id = models.CharField(blank=False, null=False,)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, blank=False, null=False, related_name='especialidade')

    def __str__(self):
        return f"Nome: {self.nome} Conselho: {self.especialidade.conselho} {self.conselho_id}"

