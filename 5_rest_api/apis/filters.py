from django_filters import rest_framework as filters  # type: ignore
from .models import School, ClassRoom


class SchoolFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']


class ClassRoomFilter(filters.FilterSet):
    school = filters.ModelChoiceFilter(queryset=School.objects.all(),
                                       field_name='schools')

    class Meta:
        model = ClassRoom
        fields = ['school']
