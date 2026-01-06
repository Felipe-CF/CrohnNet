import uuid
from django.db import models


class Especialidade(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    descricao = models.CharField(blank=False, null=False, unique=True, max_length=100)
    conselho = models.CharField(default='CRM', null=False, max_length=100)

    def __str__(self):
        return f"Especialidade: {self.descricao} Conselho: {self.conselho}"

