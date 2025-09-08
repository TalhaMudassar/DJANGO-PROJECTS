from django.urls import path
from core.views import home,contact,menu,tracking,reservation

urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('menu/',menu,name='menu'),
    path('tracking/',tracking,name='track'),
    path('reservation/',reservation,name='reservation'),  
]