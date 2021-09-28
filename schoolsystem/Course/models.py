from django.db import models

# Create your models here.
class Course(models.Model):
   course_name=models.CharField(max_length=25)
   trainer=models.CharField(max_length=19)
   course_code=models.IntegerField()
   description=models.TextField(max_length=70)

