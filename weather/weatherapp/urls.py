from django.urls import path
from weatherapp.views import home
urlpatterns = [
    path('', home , name='home'),

]

