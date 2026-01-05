from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from backend.serializer.paciente import PacienteSerializer
from backend.serializer.profissional import ProfissionalSerializer
from rest_framework.decorators import authentication_classes, permission_classes


class LoginView(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            token, created = Token.objects.get_or_create(user=usuario)

            if not created:
                token.delete()
                token = Token.objects.create(user=usuario)
            
            response_data = {
                'token': token.key,
                'username': usuario.username,
                'perfil': usuario.perfil,
            }

            usuario_data = None

            if usuario.perfil == 'pac':
                usuario_data = usuario.pac

                if usuario_data is not None:
                    usuario_response = PacienteSerializer(usuario_data).data
                    del usuario_response['user']
                        
                    response_data['dados_usuario'] = usuario_response

            elif usuario.perfil == 'pro':
                usuario_data = usuario.profissional

                usuario_response = ProfissionalSerializer(usuario_data).data

                del usuario_response['user']

                response_data['dados_usuario'] = usuario_response

            return Response(response_data)

        else:
            return Response({'mensagem': 'Login ou Senha invalido'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        header = request.headers # para fim de debugar
        token_key = request.auth.key
        token = Token.objects.get(key=token_key)
        token.delete()
        return Response({'detail': 'usuário deslogado'}, status=status.HTTP_204_NO_CONTENT)
