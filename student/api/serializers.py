
from django.db import models
from rest_framework import  serializers
from student.models import Student
from Trainer.models import Trainer
from Course.models import Course
from Event.models import Event


class StudentSerializer(serializers.ModelSerializer):
     class Meta:
              model=Student
              fields=("first_name","last_name","age")


class TrainerSerializer(serializers.ModelSerializer):
     class Meta:
              model=Trainer
              fields=("first_name","last_name","company")



class CourseSerializer(serializers.ModelSerializer):
     class Meta:
              model=Course
              fields=("course_name","trainer","course_code")



class EventSerializer(serializers.ModelSerializer):
     class Meta:
              model=Event
              fields=("name","start_time","end_time")




