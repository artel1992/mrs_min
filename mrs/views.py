from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mrs.models import *
from mrs.serializers import *

__all__ = [
    'DeanViews',
    'StudentViews',
    'TeacherViews',
    'SubjectViews',
    'GroupViews',
]


class DeanViews(ModelViewSet):
    queryset = Dean.objects.all()
    serializer_class = DeanSerializer


class StudentViews(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        return Response(data=SubjectSerializer(instance=self.get_object().subject_set.all(), many=True).data)


class TeacherViews(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectViews(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
