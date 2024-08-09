import django_filters
from .models import NetworkNode


class NetworkNodeFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(
        field_name='contact__city', lookup_expr='icontains', label='Город')
    country = django_filters.CharFilter(
        field_name='contact__country', lookup_expr='icontains', label='Страна')

    class Meta:
        model = NetworkNode
        fields = ['city', 'country']
