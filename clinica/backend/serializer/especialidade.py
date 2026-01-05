from rest_framework import serializers
from backend.models.especialidade import Especialidade

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'
        
    def create(self, validated_data):
        especialidade = Especialidade.objects.create(**validated_data)
        return especialidade
