from rest_framework import serializers
from backend.models.consulta import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
        
    def create(self, validated_data):
        consulta = Consulta.objects.create(**validated_data)
        return consulta
