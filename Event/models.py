from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Event(models.Model):
 name=models.CharField(max_length=17 ,null=True,blank=True)
 description=models.CharField(max_length=60, null=True,blank=True)
 date_of_event=models.DateField()
 start_time=models.DateTimeField(default=timezone.now)
 end_time=models.DateTimeField(default=timezone.now)
 duration=models.DateTimeField(default=timezone.now)

@property
def get_html_url(self):
    url = reverse('calendar:event_edit', args=(self.id,))
    return f'<a href="{url}"> {self.title} </a>'
 


 


 




