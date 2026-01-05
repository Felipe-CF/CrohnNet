from abc import ABC, abstractmethod
from rest_framework.permissions import IsAuthenticated, AllowAny

class PermissaoStrategy(ABC):
    @abstractmethod
    def get_permissions(self, action):
        pass

class UsuarioPermission(PermissaoStrategy):
    def get_permissions(self, action):
        if action in ['partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]

class ProfissionalPermission(PermissaoStrategy):
    def get_permissions(self, action):
        if action in ['create', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
class PacientePermission(PermissaoStrategy):
    def get_permissions(self, action):
        if action in ['partial_update', 'update', 'retrieve', 'list', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def validar(self, user):
        if user.perfil == 'admin':
            raise ValueError("Acao permitida somente para pacientes")
        
class ConsultaPermission(PermissaoStrategy):
    def get_permissions(self, action):

        if action in ['create', 'partial_update', 'retrieve', 'list', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def validar(self, user):
        if user.perfil != 'pac':
            raise ValueError("Acao permitida somente para pacientes")

class AdminPermission(PermissaoStrategy):
    def get_permissions(self, action):
        if action in ['create', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def validar(self, user):
        if user.perfil != 'admin':
            raise ValueError("Acao permitida somente para adiministradores")
        
class EspecialidadePermission(PermissaoStrategy):
    def get_permissions(self, action):
        if action in ['create', 'partial_update', 'destroy']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def validar(self, user):
        if user.perfil != 'admin':
            raise ValueError("Acao permitida somente para adiministradores")



