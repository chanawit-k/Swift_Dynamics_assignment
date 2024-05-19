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


class StudentDetailSerializer(StudentSerializer):
    classroom = ClassRoomSerializer(required=False, read_only=True)

    class Meta(StudentSerializer.Meta):
        fields = StudentSerializer.Meta.fields + ['classroom']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender']


class TeacherDetailSerializer(TeacherSerializer):
    classrooms = ClassRoomSerializer(many=True, required=False, read_only=True)

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
    teachers = TeacherSerializer(many=True, required=False)
    students = StudentSerializer(many=True, required=False)

    class Meta(ClassRoomSerializer.Meta):
        fields = ClassRoomSerializer.Meta.fields + ['teachers', 'students']
        read_only_fields = ['teachers', 'students']

    def _get_or_create_teacher(self, teachers, classroom):
        for teacher in teachers:
            item_obj, created = Teacher.objects.get_or_create(**teacher)

            classroom.teachers.add(item_obj)

    def _get_or_create_student(self, students, classroom):
        for student in students:
            item_obj, created = Student.objects.get_or_create(**student)

            classroom.students.add(item_obj)

    def update(self, instance, validated_data):
        teachers = validated_data.pop('teachers', None)
        students = validated_data.pop('students', None)

        if teachers is not None:
            instance.teachers.clear()
            self._get_or_create_teacher(teachers, instance)

        if students is not None:
            instance.students.clear()
            self._get_or_create_student(students, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
