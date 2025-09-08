from django.urls import path
from student.views import Home,candidate_detail

urlpatterns = [
    path('',Home,name='Home'),
    path('candidate/<int:pk>', candidate_detail, name='candidate_detail'),
    
]
