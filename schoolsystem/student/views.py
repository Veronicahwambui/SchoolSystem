from django import forms
from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Student
# Create your views here.
def register_student(request):
    if request.method =="POST":
        form =StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form= StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

