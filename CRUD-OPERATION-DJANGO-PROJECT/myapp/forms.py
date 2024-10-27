from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']  

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if city:
            return city.upper()  # Convert city to uppercase
        return city

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            return name.upper()  # Convert name to uppercase
        return name
