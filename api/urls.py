from  django.urls import path,include
from  rest_framework import routers
from.views import CourseViewset, EventViewset, StudentViewset, TrainerViewset

router=routers.DefaultRouter()
router.register("students/",StudentViewset)
router.register("trainers/", TrainerViewset)
router.register("courses/",CourseViewset)
router.register("events/",EventViewset)

urlpatterns=[
      path("",include(router.urls)),

]



