# Generated by Django 5.0.1 on 2024-02-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0007_resultsofoneyear_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultsofoneyear',
            name='class_name',
            field=models.CharField(max_length=255),
        ),
    ]