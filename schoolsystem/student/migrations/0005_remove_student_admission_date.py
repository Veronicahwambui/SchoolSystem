# Generated by Django 3.2.4 on 2021-08-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_admission_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='admission_date',
        ),
    ]
