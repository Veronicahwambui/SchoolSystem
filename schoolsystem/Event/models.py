from django.db import models

# Create your models here.
class Event(models.Model):
 name=models.CharField(max_length=17)
 location=models.CharField(max_length=20)
 date_of_event=models.DateField()
 time=models.DateTimeField()
 duration=models.DateTimeField()




