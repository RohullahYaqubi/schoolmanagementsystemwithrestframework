from django.db import models

class Teacher(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.name} {self.last_name}'

class Student(models.Model):

    STATUS_ACTIVE = 'A'
    STATUS_INACTIVE = 'I'
    ACTIVE_STATUS = [
        (STATUS_ACTIVE, 'ACTIVE'),
        (STATUS_INACTIVE, 'INACTIVE')
    ]
    student_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    grandfather_name = models.CharField(max_length=255)
    number_of_tazkira = models.PositiveIntegerField(blank=True)
    status = models.CharField(max_length=1, choices=ACTIVE_STATUS, default=STATUS_ACTIVE, null=False )
    class_name = models.ForeignKey("NameOfClass", on_delete=models.PROTECT, related_name='student')


    def __str__(self) -> str:
        return f'{self.name} {self.father_name}'


class NameOfClass(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.OneToOneField("Teacher", on_delete=models.PROTECT, related_name='name_of_class')

    def __str__(self) -> str:
        return self.name


class Attendence(models.Model):
    ATTENDENCE_STATUS_PRESENT = 'P'
    ATTENDENCE_STATUS_ABSENT = 'A'
    ATTENDENCE_STATUS = [
        (ATTENDENCE_STATUS_PRESENT, 'PRESENT'),
        (ATTENDENCE_STATUS_ABSENT, 'ABSENT')
    ]
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    attendence_status = models.CharField(max_length=1, choices=ATTENDENCE_STATUS,
                                          default=ATTENDENCE_STATUS_ABSENT)
    


class ResultsOfOneYear(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    class_name = models.ForeignKey(NameOfClass, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    maths = models.PositiveSmallIntegerField()
    litriture = models.PositiveSmallIntegerField()
    physics = models.PositiveSmallIntegerField()
    geology = models.PositiveSmallIntegerField()
    chemistry = models.PositiveIntegerField()
    total_number = models.PositiveIntegerField()
