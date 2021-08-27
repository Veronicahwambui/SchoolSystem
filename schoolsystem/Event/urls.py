
from django.urls import path
from.views import register_event,event_list


urlpatterns =[
    path("register/",register_event,name="register_event"),
    path("list/",event_list, name="event_list"),

]