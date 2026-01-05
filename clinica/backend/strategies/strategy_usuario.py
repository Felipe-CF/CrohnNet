from abc import ABC, abstractmethod
from rest_framework.exceptions import PermissionDenied

class UsuarioStrategy(ABC):
    @abstractmethod
    def validar_usuario(self, perfil):
        pass

class ProfissionalStrategy(UsuarioStrategy):
    def validar_usuario(self, request):
        profissional = getattr(request.user, 'pro', None)
        if not profissional:
            raise PermissionDenied("Usuario não é um profissional") 
        return profissional  

class AdminStrategy(UsuarioStrategy):
    def validar_usuario(self, request):
        admin = getattr(request.user, 'admin', None)
        if not admin:
            raise PermissionDenied("Usuario não é um admin") 
        return admin  

class PacienteStrategy(UsuarioStrategy):
    def validar_usuario(self, request):
        paciente = getattr(request.user, 'pac', None)
        if not paciente:
            raise PermissionDenied("Usuario não é um paciente") 
        return paciente  

class ConsultaStrategy():

    def validar_agendamento(self, request):
        paciente = getattr(request.user, 'pac', None)

        if not paciente:
            raise PermissionDenied("Usuario não é um paciente") 
        
        return paciente  
    
    def validar_consulta(self, request):
        profissional = getattr(request.user, 'pro', None)

        if not profissional:
            raise PermissionDenied("Usuario não é um profissional") 
        
        return profissional  
    
    def validar_alteracao(self, request):
        paciente = getattr(request.user, 'pac', None)

        if not paciente:
            profissional = getattr(request.user, 'pro', None)

            if not profissional:
                raise PermissionDenied("Usuario não pode acessar a consulta") 
            
            return profissional

        return paciente
      
        

