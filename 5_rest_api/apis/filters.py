from django_filters import rest_framework as filters
from .models import School, ClassRoom, Teacher, Student


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


class TeacherFilter(filters.FilterSet):
    school = filters.CharFilter(method='filter_by_school')
    classroom = filters.ModelChoiceFilter(queryset=ClassRoom.objects.all(),
                                          field_name='classrooms')
    first_name = filters.CharFilter(field_name='first_name',
                                    lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='last_name',
                                   lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender', lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']

    def filter_by_school(self, queryset, name, value):
        return queryset.filter(classrooms__schools__id=value).distinct()


class StudentFilter(filters.FilterSet):
    school = filters.CharFilter(method='filter_by_school')
    classroom = filters.CharFilter(field_name='classroom', lookup_expr='exact')
    first_name = filters.CharFilter(field_name='first_name',
                                    lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='last_name',
                                   lookup_expr='icontains')
    gender = filters.CharFilter(field_name='gender', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['school', 'classroom', 'first_name', 'last_name', 'gender']

    def filter_by_school(self, queryset, name, value):
        return queryset.filter(classroom__schools__id=value).distinct()
