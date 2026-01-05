from rest_framework import serializers
from backend.models.paciente import Paciente
from backend.serializer.usuario import UsuarioSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
        
    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')

        usuario_serializer = UsuarioSerializer(data=usuario_data)

        usuario_serializer.is_valid(raise_exception=True)

        novo_usuario = usuario_serializer.save()

        paciente = Paciente.objects.create(user=novo_usuario, **validated_data)

        return paciente
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data) 
        
        return instance

