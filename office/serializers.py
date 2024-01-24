from rest_framework import serializers
from .models import Student, NameOfClass, Teacher


class SimpleStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name']


class ClassNameRetriveSerializer(serializers.ModelSerializer):
    student = SimpleStudentSerializer(many=True)
    class Meta:
        model = NameOfClass
        fields = ['id','name', 'teacher','student']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'father_name', 'grandfather_name', 'number_of_tazkira', 'class_name']


class ClassNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NameOfClass
        fields = ['id','name', 'teacher']



class TeacherSerializer(serializers.ModelSerializer):
    name_of_class = serializers.CharField(read_only= True)
    class Meta:
        model = Teacher
        fields = ['employee_id', 'name', 'last_name', 'date_joined', 'name_of_class']





