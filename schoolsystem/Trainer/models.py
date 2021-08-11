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
  resume=models.FileField()
  salary=models.PositiveBigIntegerField()
  image=models.ImageField()
  contract=models.FileField()

