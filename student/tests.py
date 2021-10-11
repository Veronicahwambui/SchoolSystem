
from django.test import TestCase
from .models import Student 
import datetime
from django.urls import reverse
# Create your tests here.

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="Celine", last_name="Gushima",age=21, student_id="344556we",class_name="Lovelace",email="celinegushima@gmail",phone_number=78965443)
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student .first_name,self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student .last_name,self.student.full_name())
    
    def test_year_of_birth(self):
        curreny_year= datetime.datetime.now().age
        year= curreny_year-self.student.age
        self.assertEqual(year, self.student.year_of_birth())

    def test_student_registration_view(self):
        url=reverse("register_student")
        data={"first-name":self.student.first_name,"last-name":self.student.last_name,"age":self.student.age,"student_id":self.student.student_id,"class-name":self.student.class_name,"email":self.student.email,"phone_number":self.student.phone_number}
        request =self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    


       