from rest_framework import serializers
from backend.models.profisssional import Profissional
from backend.serializer.usuario import UsuarioSerializer


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')

        usuario_serializer = UsuarioSerializer(data=usuario_data)

        usuario_serializer.is_valid(raise_exception=True)

        novo_usuario = usuario_serializer.save()

        profissional = Profissional.objects.create(user=novo_usuario, **validated_data)

        return profissional
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data) 
        
        return instance

        # # --- Lógica Manual para o campo 'bio' ---
        
        # # Exemplo: Se 'nome_completo' foi alterado, atualize a 'bio'
        # if 'nome_completo' in validated_data:
        #     novo_nome = validated_data.get('nome_completo')
        #     instance.bio = f"A bio foi atualizada em função da mudança de nome para {novo_nome}."
        #     instance.save() # Salva o campo 'bio' manualmente