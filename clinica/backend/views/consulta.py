from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from backend.filters.consulta_filters import ConsultaFilter
from django_filters.rest_framework import DjangoFilterBackend
from backend.strategies.strategy_usuario import ConsultaStrategy 
from backend.strategies.strategy_permissions import ConsultaPermission
from backend.serializer.consulta import ConsultaSerializer, Consulta 


class ConsultaView(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filterset_class = ConsultaFilter
    filter_backends = [DjangoFilterBackend]
    search_fields = ['conteudo', 'data_criacao', 'status', 'tag']
    ordering_fields = ['data_criacao']
    permission_strategy = ConsultaPermission()
    usuario_strategy = ConsultaStrategy()

    def get_permissions(self): # sobrescreve o método padrão de permissões do DRF
        return self.permission_strategy.get_permissions(self.action)

    def create(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_agendamento(request)

            serializer = ConsultaSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_agendamento(request)

            # Recupera o objeto com o metodo do ModelViewSet que usa 'lookup_field' usando o valor passado na URL
            item = self.get_object()
            serializer = self.get_serializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Http404:
            return Response({'erro': 'Objeto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_agendamento(request)

            itens = self.filter_queryset(self.get_queryset())

            if not itens.exists():
                return Response({'mensagem': 'Nenhuma Consulta encontrada'}, status=status.HTTP_200_OK)
            
            serializer = self.get_serializer(itens, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, *args, **kwargs):
        try:
            self.usuario_strategy.validar_agendamento(request)

            if 'consulta_id' in request.data:
                item = get_object_or_404(Consulta, id=request.data.get("consulta_id"))

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
            self.usuario_strategy.validar_agendamento(request)

            if 'consulta_id' in request.data:
                item = get_object_or_404(Consulta, id=request.data.get("consulta_id"))

                item.delete()

                return Response({'mensagem': 'Consulta deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
            
            return Response({"erro": "Campos obrigatórios ausentes na requisição"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Exception as e:
            return Response({'erro': 'Problema na API'}, status=status.HTTP_404_NOT_FOUND)
