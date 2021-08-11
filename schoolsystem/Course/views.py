from .forms import CourseRegistrationForm
from django.forms import forms
from django.shortcuts import render


# Create your views here.
def register_course(request):
    if request. method=="POST":
        form =CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            print(form.errors)
    else:
        form =CourseRegistrationForm()
    return render(request ,"register_course.html", {"form":form})
