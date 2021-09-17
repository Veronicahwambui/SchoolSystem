
from django.forms import forms
from django.shortcuts import render,redirect
from .models import Course
from .forms import CourseRegistrationForm


# Create your views here.
def register_course(request):
    if request. method=="POST":
        form =CourseRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

        else:
            print(form.errors)
    else:
        form =CourseRegistrationForm()
    return render(request ,"register_course.html", {"form":form})

def course_list(request):
    courses=Course.objects.all()
    return render(request,"course_list.html",{"courses":courses})

def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=CourseRegistrationForm(request.Post,instance=course)
        if form .is_valid():
            form.save()

    else:
        form=CourseRegistrationForm(instance=course)
        return render(request,"edit_course.html",{"form":form})

def course_profile(request,id):
    course=Course.objects.get(id=id)
    return render(request,"course_profile.html",{"course":course})



def delete_course(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect("course_list")