from django.db import models

# Create your models here.
class Trainer(models.Model):
  first_name=models.CharField(max_length=15)
  last_name=models.CharField(max_length=16)
  trainer_id=models.CharField(max_length=18)
  phone_number=models.CharField(max_length=20)
  email=models.EmailField()
  gender_choice=((u'F',u'female'),(u'm',u'male'),(u'o','other'))
  gender=models.CharField(max_length=16,choices=gender_choice)
  company=models.CharField(max_length=18)
  resume=models.FileField(upload_to="files/", blank=True,null=True)
  salary=models.BigIntegerField(null=True)
  image=models.ImageField(upload_to="Images/",blank=True ,null=True)
  contract=models.FileField(upload_to="files/", blank=True,null=True)

