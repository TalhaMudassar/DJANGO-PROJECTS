from django.contrib import admin
from django.urls import path, include  # Make sure to include 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Your app's URLs
]
