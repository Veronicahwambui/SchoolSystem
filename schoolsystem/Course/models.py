from django.db import models

# Create your models here.
class Course(models.Model):
   Course_name=models.CharField(max_length=18)
   Trainer=models.CharField(max_length=19)
   Course_code=models.IntegerField()
   description=models.TextField(max_length=70)

