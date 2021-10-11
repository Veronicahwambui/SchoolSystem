from django import forms
from django.db import models
from django.db.models.base import Model
from.models import Event
from django.forms import fields


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"