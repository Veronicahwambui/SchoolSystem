from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateTimeField()
    student_email=models.EmailField(max_length=30)
    phone_number=models.CharField(max_length=18)
    student_id=models.CharField(max_length=16)
    class_name=models.CharField(max_length=10)
    gender_choice=((u'F',u'female'),(u'm',u'male'),(u'o','other'))
    gender=models.CharField(max_length=10,choices=gender_choice)
    nationality_choice=((u'E',u'Rwanda'), (u'K',u'Kenya'),(u'U','Uganda'))
    nationality=models.CharField(max_length=15,choices=nationality_choice)
    city=models.CharField(max_length=12)
    admission_date=models.DateTimeField()
    guardian_name=models.CharField(max_length=15)
    guardian_phone_number=models.CharField(max_length=18)
    academic_year=models.DateTimeField()
    profile_pic=models.ImageField(upload_to="Images")
    medical_report=models.FileField(upload_to="files")
   
  
   