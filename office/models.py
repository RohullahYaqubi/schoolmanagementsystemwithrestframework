from django.db import models
from django.core.validators import MaxValueValidator

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
    status = models.CharField(max_length=1, choices=ACTIVE_STATUS, default=STATUS_ACTIVE)
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
    
    def __str__(self) -> str:
        return str(self.student)
    


class ResultsOfOneYear(models.Model):
    MID_TERM = 'M'
    LAST_TERM = 'L'
    TERM = [
        (MID_TERM, 'MID TERM'),
        (LAST_TERM, 'LAST TERM')
    ]
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    class_name = models.CharField(max_length=255)
    term = models.CharField(max_length=1, choices=TERM, default=MID_TERM)
    date_created = models.DateField(auto_now_add=True)
    maths = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    litriture = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    physics = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    geology = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    chemistry = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    edification = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(100)])
    total_number = models.PositiveIntegerField(null=True)
    percentage = models.FloatField(null=True, validators=[MaxValueValidator(100)])
    

    def save(self, *args, **kwargs):
        self.total_number = self.maths + self.litriture + self.physics + self.geology + self.chemistry + self.edification
        self.percentage = (self.total_number / 600) * 100
        self.class_name = str(self.student.class_name)
        super().save(*args, **kwargs)


        def __str__(self) -> str:
            return self.student



class FeesOfStudents(models.Model):
    PAYMENT_STATUS_UNPAID = 'U'
    PAYMENT_STATUS_PAID = 'P'
    PAYMENT_STATUS = [
        (PAYMENT_STATUS_UNPAID, 'UNPAID'),
        (PAYMENT_STATUS_PAID, 'PAID')
    ]

    FEE_TYPE_GUARD = 'G'
    FEE_TYPE_FIRST_EXAMS = 'FREX'
    FEE_TYPE_SECOND_EXAMS = 'SCEX'
    FEE_TYPE_MONTHLY_FEES = 'MF'
    FEE_TYPE_FIRST_KANKOR = 'FRK'
    FEE_TYPE_SECOND_KANKOR = 'SEK'

    FEES_TYPE = [
        (FEE_TYPE_GUARD, 'GUARD'),
        (FEE_TYPE_FIRST_EXAMS, 'FIRST EXAMS'),
        (FEE_TYPE_SECOND_EXAMS, 'SECOND_EXAMS'),
        (FEE_TYPE_MONTHLY_FEES, 'MONTHLY_FEES'),
        (FEE_TYPE_FIRST_KANKOR, 'FIRST_KANKOR'),
        (FEE_TYPE_SECOND_KANKOR, 'SECOND_KANKOR'),
    ]

    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=255)
    fees_type = models.CharField(max_length=4, choices=FEES_TYPE, default=FEE_TYPE_MONTHLY_FEES)
    amount_paid = models.PositiveSmallIntegerField()
    amount_to_pay = models.PositiveSmallIntegerField()
    date_of_payment = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_UNPAID)


    def save(self, *args, **kwargs):
        self.class_name = str(self.student.class_name)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return str(self.student)




