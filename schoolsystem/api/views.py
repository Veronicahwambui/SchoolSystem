
from django.http.request import QueryDict
from django.shortcuts import render
from  rest_framework import viewsets
from student.models import Student
from Trainer.models import Trainer
from Course.models import Course
from Event .models import Event
from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CourseSerializer 
from .serializers import EventSerializer




# Create your views here.
class  StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class TrainerViewset(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer


class CourseViewset(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer


