import django_filters
from backend.models.consulta import Consulta


class ConsultaFilter(django_filters.FilterSet):
    nome_paciente = django_filters.CharFilter(
        field_name='consulta_paciente.nome', 
        lookup_expr='exact'
        )

    nome_profissional = django_filters.CharFilter(
        field_name='consulta_profissional.nome', 
        lookup_expr='exact'
        )

    data_criacao = django_filters.DateFilter(
        field_name='data_criacao', 
        lookup_expr='gte'
        )

    data_consulta = django_filters.DateFilter(
        field_name='data_consulta', 
        lookup_expr='gte'
        )

    status_confirmacao = django_filters.BooleanFilter(
        field_name='status_confirmacao', 
        lookup_expr='exact'
        )

    class Meta:
        model = Consulta
        fields = ['nome_paciente', 'nome_profissional', 'data_criacao', 'data_consulta', 'status_confirmacao']