# Generated by Django 5.0.1 on 2024-02-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_resultsofoneyear_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultsofoneyear',
            name='term',
            field=models.CharField(choices=[('M', 'MID TERM'), ('L', 'LAST TERM')], default='M', max_length=1),
        ),
    ]
