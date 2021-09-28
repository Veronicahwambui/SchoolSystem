from django import forms
from django.shortcuts import render,redirect
from .forms import TrainerRegistrationForm
from .models import Trainer

# Create your views here.
def register_trainer(request):
    if  request.method == "POST":
        form=TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

        else:
            print(form.errors)
    else:
        form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})


def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})



def edit_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    if request.method=="POST":
        form=TrainerRegistrationForm(request.Post,instance=trainer)
        if form.is_valid():
            form.save()

    else:
        form=TrainerRegistrationForm(instance=trainer)
        return render(request,"edit_trainer.html",{"form":form})


def trainer_profile(request,id):
    trainer=Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})



def delete_trainer(request,id):
    trainer=Trainer.objects.get(id=id)
    trainer.delete()
    return redirect("trainer_list")

