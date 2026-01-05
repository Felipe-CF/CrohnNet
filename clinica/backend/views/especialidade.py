from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from backend.strategies.strategy_usuario import AdminStrategy
from backend.strategies.strategy_permissions import EspecialidadePermission
from backend.serializer.especialidade import EspecialidadeSerializer, Especialidade 


class EspecialidadeView(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    ordering_fields = ['data_criacao']
    permission_strategy = EspecialidadePermission()
    usuario_strategy = AdminStrategy()

    def get_permissions(self): # sobrescreve o método padrão de permissões do DRF
        return self.permission_strategy.get_permissions(self.action)

    def create(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)

            serializer = EspecialidadeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)

            item = self.get_object()

            serializer = self.get_serializer(item)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Http404:
            return Response({'erro': 'Objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            itens = self.get_queryset()

            if not itens.exists():
                return Response({'mensagem': 'Nenhuma especialidade encontrada'}, status=status.HTTP_200_OK)
            
            serializer = self.get_serializer(itens, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)

            if 'especialidade_id' in request.data:
                item = get_object_or_404(Especialidade, id=request.data.get("especialidade_id"))

                # Atualiza parcialmente o objeto
                serializer = self.get_serializer(item, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': 'Problema na API'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_usuario(request)

            if 'especialidade_id' in request.data:
                item = get_object_or_404(Especialidade, id=request.data.get("especialidade_id"))

                item.delete()

                return Response({'mensagem': 'Especialidade deletada com sucesso'}, status=status.HTTP_204_NO_CONTENT)
            
            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': 'Problema na API'}, status=status.HTTP_404_NOT_FOUND)
