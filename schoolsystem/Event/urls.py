

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cal'

urlpatterns = [  
    
    path('cal/', views.CalendarView.as_view(), name='calendar'),
    url('list/', views.event, name='event_new'),
	url('edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),  
]


