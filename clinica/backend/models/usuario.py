import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    PERFIL=(
        ('pro', 'Profissional'),
        ('pac', 'Paciente'),
        ('admin', 'Administrador'),
        ('atend', 'Atendente'),
    )
    perfil = models.CharField(max_length=20, choices=PERFIL)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.username + ' ' + self.perfil