from django.db import models
import datetime
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField(null=True)
    email=models.EmailField()
    phone_number=models.CharField(max_length=18)
    student_id=models.CharField(max_length=16)
    class_name=models.CharField(max_length=10)
    gender_choice=((u'F',u'female'),(u'm',u'male'),(u'o','other'))
    gender=models.CharField(max_length=10,choices=gender_choice)
    nationality_choice=((u'E',u'Rwanda'), (u'K',u'Kenya'),(u'U','Uganda'))
    nationality=models.CharField(max_length=15,choices=nationality_choice)
    city=models.CharField(max_length=12)
    guardian_name=models.CharField(max_length=15)
    guardian_phone_number=models.CharField(max_length=18)
    academic_year=models.BigIntegerField(null=True,blank=True)
    images=models.ImageField(upload_to="Images/",blank=True ,null=True) 
    medical_report=models.FileField(upload_to="files/", blank=True,null=True)



    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def year_of_birth(self):
        return 2021-self.age
   
  
   