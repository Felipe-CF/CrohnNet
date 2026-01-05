from rest_framework import serializers
from backend.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'perfil', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        usuario = Usuario.objects.create(**validated_data)
        return usuario
