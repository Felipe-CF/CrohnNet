import uuid
from django.db import models


class Endereco(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    municipio = models.CharField(blank=False, null=False, max_length=255)
    bairro = models.CharField(blank=False, null=False, max_length=255)
    rua = models.CharField(blank=False, null=False, max_length=255)
    numero = models.CharField(blank=False, null=False, max_length=20)

    def __str__(self):
        return (
            f"Endereco: {self.municipio}-{self.bairro}, "
            f"{self.rua}, {self.numero}"
        )
