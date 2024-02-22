from rest_framework import serializers
from .models import Student, NameOfClass, Teacher, Attendence, ResultsOfOneYear


class SimpleStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name']


class ClassNameRetrieveSerializer(serializers.ModelSerializer):
    student = SimpleStudentSerializer(many=True)
    number_of_students = serializers.SerializerMethodField()
    class Meta:
        model = NameOfClass
        fields = ['id', 'name', 'teacher', 'number_of_students', 'student']

    def get_number_of_students(self, instance):
        students = self.context['students_in_class']
        number_of_students = students.count()

        return number_of_students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'father_name', 'grandfather_name', 'number_of_tazkira', 'class_name', 'status']


class ClassNameSerializer(serializers.ModelSerializer):
    number_of_students = serializers.SerializerMethodField()
    class Meta:
        model = NameOfClass
        fields = ['id', 'name', 'teacher', 'number_of_students']

    def get_number_of_students(self, obj):
        number_of_students = obj.student.count()
        return number_of_students



class TeacherSerializer(serializers.ModelSerializer):
    name_of_class = serializers.CharField(read_only= True)
    class Meta:
        model = Teacher
        fields = ['employee_id', 'name', 'last_name', 'date_joined', 'name_of_class']



class AttendenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ['id', 'student', 'date','attendence_status']


class AttendenceCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ['student','attendence_status']


def getting_students_group(percentage):
    if percentage >=90:
        return 'A+'
    elif percentage >=80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    else: 
        return 'F'
    

class ResultsOfStudentSerializer(serializers.ModelSerializer): 
    group = serializers.SerializerMethodField()
    class Meta:
        model = ResultsOfOneYear
        fields = ['id', 'student', 'class_name', 'date_created', 'term', 'maths', 'litriture', 'physics', 'geology', 'chemistry', 'edification', 'total_number', 'percentage', 'group']

    def get_group(self, obj):
        percentage = obj.percentage
        if percentage >=90:
            return 'A'
        elif percentage >=80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        else:
            return 'F'

class CreateResultsOfStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsOfOneYear
        fields = ['id', 'student', 'term', 'maths', 'litriture', 'physics', 'geology', 'chemistry', 'edification']