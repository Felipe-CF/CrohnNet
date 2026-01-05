from rest_framework import serializers
from backend.models.endereco import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
        
    def create(self, validated_data):
        endereco = Endereco.objects.create(**validated_data)
        return endereco
