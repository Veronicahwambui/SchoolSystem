from django.urls import path
from.views import register_course,course_list



urlpatterns =[
    path("register/",register_course ,name="register_course"),
    path("list/",course_list, name="course_list"),
]