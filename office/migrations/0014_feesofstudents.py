# Generated by Django 5.0.1 on 2024-02-22 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0013_alter_resultsofoneyear_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeesOfStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=255)),
                ('fees_type', models.CharField(choices=[('G', 'GUARD'), ('FREX', 'FIRST EXAMS'), ('SCEX', 'SECOND_EXAMS'), ('MF', 'MONTHLY_FEES'), ('FRK', 'FIRST_KANKOR'), ('SEK', 'SECOND_KANKOR')], default='MF', max_length=4)),
                ('amount_paid', models.PositiveSmallIntegerField()),
                ('amount_to_pay', models.PositiveSmallIntegerField()),
                ('date_of_payment', models.DateField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('U', 'UNPAID'), ('P', 'PAID')], default='U', max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.student')),
            ],
        ),
    ]