from rest_framework import serializers
from apis.models import School, Teacher, Student, ClassRoom
from drf_spectacular.utils import extend_schema_field


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'year', 'section']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']


class TeacherDetailSerializer(TeacherSerializer):
    classrooms = ClassRoomSerializer(many=True, read_only=True)

    class Meta(TeacherSerializer.Meta):
        model = Teacher
        fields = TeacherSerializer.Meta.fields + ['classrooms']


class SchoolSerializer(serializers.ModelSerializer):
    """Serializer for School."""
    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address']
        read_only_fields = ['id']


class SchoolDetailSerializer(SchoolSerializer):
    """Serializer for School Detail view."""
    number_classrooms = serializers.SerializerMethodField()
    number_teacher = serializers.SerializerMethodField()
    number_student = serializers.SerializerMethodField()

    class Meta(SchoolSerializer.Meta):
        fields = SchoolSerializer.Meta.fields + ['number_classrooms',
                                                 'number_teacher',
                                                 'number_student']

    @extend_schema_field(serializers.IntegerField)
    def get_number_classrooms(self, obj):
        return obj.classrooms.count()

    @extend_schema_field(serializers.IntegerField)
    def get_number_teacher(self, obj):
        return Teacher.objects.filter(classrooms__schools=obj).distinct()\
                .count()

    @extend_schema_field(serializers.IntegerField)
    def get_number_student(self, obj):
        return Student.objects.filter(classroom__schools=obj).distinct()\
                .count()


class ClassRoomDetailSerializer(ClassRoomSerializer):
    """Serializer for School Detail view."""
    teachers = TeacherSerializer(many=True)
    students = StudentSerializer(many=True)

    class Meta(ClassRoomSerializer.Meta):
        fields = ClassRoomSerializer.Meta.fields + ['teachers', 'students']
        read_only_fields = ['teachers', 'students']
