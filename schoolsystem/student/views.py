from django import forms
from django.shortcuts import render
from .forms import StudentRegistrationForm

# Create your views here.
def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

