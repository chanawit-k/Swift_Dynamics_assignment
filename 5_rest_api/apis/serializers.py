from rest_framework import serializers  # type: ignore
from apis.models import School, Teacher, Student, ClassRoom


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'sex']


class SchoolSerializer(serializers.ModelSerializer):
    """Serializer for School."""

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']
        read_only_fields = ['id']

    def get_number_classrooms(self, obj):
        return obj.classrooms.count()

    def get_number_teacher(self, obj):
        return Teacher.objects.filter(classrooms__schools=obj).distinct()\
                .count()

    def get_number_student(self, obj):
        return Student.objects.filter(classroom__schools=obj).distinct()\
                .count()


class SchoolDetailSerializer(SchoolSerializer):
    """Serializer for School Detail view."""
    number_classrooms = serializers.SerializerMethodField()
    number_teacher = serializers.SerializerMethodField()
    number_student = serializers.SerializerMethodField()

    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields + ['number_classrooms',
                                                 'number_teacher',
                                                 'number_student']

    def get_number_classrooms(self, obj):
        return obj.classrooms.count()

    def get_number_teacher(self, obj):
        return Teacher.objects.filter(classrooms__schools=obj).distinct()\
                .count()

    def get_number_student(self, obj):
        return Student.objects.filter(classroom__schools=obj).distinct()\
                .count()


class ClassRoomSerializer(SchoolSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'year', 'section']
