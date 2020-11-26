from rest_framework.serializers import *

from mrs.models import *

__all__ = [
    'DeanSerializer',
    'StudentSerializer',
    'TeacherSerializer',
    'SubjectSerializer',
    'GroupSerializer',
]


class DeanSerializer(ModelSerializer):
    class Meta:
        model = Dean
        fields = [
            'last_name',
            'first_name',
            'father_name',
            'faculty_title',
        ]


class StudentSerializer(ModelSerializer):
    group = PrimaryKeyRelatedField(queryset=Group.objects.all())
    group_number = StringRelatedField(source='group')

    class Meta:
        model = Student
        fields = [
            'last_name',
            'first_name',
            'father_name',
            'group',
            'group_number',
        ]


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            'last_name',
            'first_name',
            'father_name',
        ]


class SubjectSerializer(ModelSerializer):
    teacher = PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    students = PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = Subject
        fields = [
            'title',
            'teacher',
            'students'
        ]


class GroupSerializer(ModelSerializer):
    dean = PrimaryKeyRelatedField(queryset=Dean.objects.all())
    students = StringRelatedField(many=True, read_only=True, source='student_set')

    class Meta:
        model = Group
        fields = [
            'course_number',
            'dean',
            'group_number',
            'students',
        ]
