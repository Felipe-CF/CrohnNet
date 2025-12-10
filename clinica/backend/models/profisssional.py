import uuid
from django.db import models
from .especialidade import Especialidade
from backend.models.usuario import Usuario


class Profissional(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    nome = models.CharField(blank=False, null=False, max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    contato = models.CharField(default='sem telefone', null=False, max_length=50)
    cpf = models.CharField(max_length=11, blank=False, null=False)

    user = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='usuario_pro',
    )

    conselho_id = models.CharField(blank=False, null=False, max_length=50)

    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='profissionais',
    )

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Conselho: {self.especialidade.conselho} {self.conselho_id}"
        )
