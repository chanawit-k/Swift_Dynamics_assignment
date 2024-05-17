from django_filters import rest_framework as filters  # type: ignore
from .models import School


class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']
