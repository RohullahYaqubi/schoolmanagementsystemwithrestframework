from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .serializers import StudentsSerializer, ClassNameSerializer, TeacherSerializer
from .models import Student, NameOfClass, Teacher


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_of_class']
    
    def destroy(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        try:
            class_name = NameOfClass.objects.get(teacher=teacher.employee_id)
            return Response('This teacher cannot be deleted because he is associated with a class_lesson. To delete his record, please remove him from the territory of the class.',
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except NameOfClass.DoesNotExist:
            teacher.delete()
            return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
        


class NameOfClassViewset(ModelViewSet):
    queryset = NameOfClass.objects.all()
    serializer_class = ClassNameSerializer


    def destroy(self, request, pk):
        class_name = get_object_or_404(NameOfClass, pk=pk)
        try:
            teacher = Teacher.objects.get(name_of_class=class_name)
            query_set = Student.objects.filter(class_name=class_name)
            return Response('this class cannot be deleted beacuse it is accosiated with teacher or students')
        except (Teacher.DoesNotExist, Student.DoesNotExist):
            class_name.delete()
            return Response('Deleted', status=status.HTTP_204_NO_CONTENT)



class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.select_related('class_name').all()
    serializer_class = StudentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['class_name']


    def perform_create(self, serializer):
        instance = serializer.save()
        class_name = instance.class_name
        class_name.number_of_students += 1
        class_name.save()








