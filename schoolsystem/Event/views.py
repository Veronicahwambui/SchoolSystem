from django.shortcuts import render
from .forms import EventRegistrationForm
from django import forms

# Create your views here.
def register_event(request):
    if request.method=="POST":
       form=EventRegistrationForm(request.POST)
       if form.is_valid():
            form.save()
       else:
            print(form.errors)
    else:
        form= EventRegistrationForm()
    return render(request,"register_event.html",{"form":form})
