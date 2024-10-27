# myapp/urls.py
from django.urls import path
from .views import Home, AddStudent, DeleteaStudent,Editstudent

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-student/', AddStudent.as_view(), name='add-student'),
    path('delete-student/', DeleteaStudent.as_view(), name='delete-student'),
    path('edit-student/<int:id>/',Editstudent.as_view(),name='edit-student')
]
