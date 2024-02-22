from django.shortcuts import get_object_or_404
from django.http import QueryDict
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import (StudentsSerializer, 
                          ClassNameSerializer, 
                          TeacherSerializer,
                           ClassNameRetrieveSerializer, 
                           AttendenceSerializers, 
                           AttendenceCreateSerializers,
                           ResultsOfStudentSerializer,
                           CreateResultsOfStudentSerializer)
from .models import Student, NameOfClass, Teacher, Attendence, ResultsOfOneYear


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.select_related('name_of_class').all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_of_class']
    
    def destroy(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        try:
            class_name = NameOfClass.objects.filter(teacher=teacher.employee_id)
            return Response('This teacher cannot be deleted because he is associated with a class_lesson. To delete his record, please remove him from the territory of the class.',
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except NameOfClass.DoesNotExist:
            teacher.delete()
            return Response('Deleted', status=status.HTTP_204_NO_CONTENT)
        

 
class NameOfClassViewset(ModelViewSet):
    http_method_names = ['get','post', 'put', 'delete', 'head', 'options']
    queryset = NameOfClass.objects.prefetch_related('student').all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher']


    def get_serializer_class(self):

        if self.action == 'retrieve':
            return ClassNameRetrieveSerializer
        return ClassNameSerializer
    
    def get_serializer_context(self):
        if self.action == 'retrieve':
            class_name = get_object_or_404(NameOfClass, pk = self.kwargs.get('pk'))
            students_in_class = Student.objects.filter(class_name=class_name)
            return {'students_in_class':students_in_class}
        else:
            return {'class_names':self.queryset}
        
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
    http_method_names = ['get','post', 'put', 'head', 'options']
    queryset = Student.objects.select_related('class_name').all()
    serializer_class = StudentsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['class_name', 'status']


class AttendenceViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']

    
    def get_queryset(self):
        queryset = Attendence.objects.filter(student_id = self.kwargs['students_pk'])
        return queryset
    
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AttendenceCreateSerializers
        return AttendenceSerializers
       
    
    def create(self, request, *args, **kwargs):
        student_id = self.kwargs['students_pk']
        curent_date = timezone.now()
        attendence_date = curent_date.date()
        print(attendence_date)
        
        try:
            existing_attendence = Attendence.objects.get(student=student_id, date=attendence_date)
            print(existing_attendence)
            return Response('This student already has an attendance for the given date', status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        except Attendence.DoesNotExist:
            data = QueryDict(request.data.urlencode(), mutable=True)
            data['student'] = student_id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ResultsOfStudentsViewSet(ModelViewSet):
    http_method_names = ['get','post', 'patch', 'head', 'options']

    def get_queryset(self):
        queryset = ResultsOfOneYear.objects.filter(student = self.kwargs['student_pk'])
        return queryset


    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH':
            return CreateResultsOfStudentSerializer
        return ResultsOfStudentSerializer


    def create(self, request, *args, **kwargs):
        student_id = self.kwargs['student_pk']
        term = request.data.get('term')

        try:
            student = Student.objects.get(pk=student_id)
            class_of_student = student.class_name
            existing_result = ResultsOfOneYear.objects.get(student=student_id, class_name=class_of_student, term=term)
            return Response(f'The result for student name : {student.name}, class : {class_of_student} and Term : {term}  already exists', status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        except ResultsOfOneYear.DoesNotExist:
            data = QueryDict(request.data.urlencode(), mutable=True)
            data['student'] = student_id
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
        

    

    

        
    

