from django.db import models

# Create your models here.
class Event(models.Model):
 name=models.CharField(max_length=17)
 location=models.CharField(max_length=20)
 date_of_event=models.DateField()
 start_and_end=models.DateTimeField()
 duration=models.DateTimeField()
 link_of_event=models.CharField(max_length=23)

 




