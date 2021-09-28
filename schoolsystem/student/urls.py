from django.urls import path
from.views import register_student,student_list,edit_student, student_profile,delete_student

urlpatterns=[
    path("register/",register_student,name="register_student"),
    path("list/",student_list, name="student_list"),
    path("edit/<int:id>/",edit_student,name="edit_student"),
    path("profile/<int:id>/",student_profile,name="student_profile"),
    path("delete/<int:id>/",delete_student,name="delete_student")

]