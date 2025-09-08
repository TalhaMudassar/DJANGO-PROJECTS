from django import forms 
from student.models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)
JOB_CITY_CHOICE = [
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Ranchi', 'Ranchi')    ,
    ('Mumbai', 'Mumbai'),
    ('Dhanbad', 'Dhanbad'),
    ('Bangalore', 'Bangalore'),
]

class ProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES, required=False)
    job_city = forms.MultipleChoiceField(choices = JOB_CITY_CHOICE) #here is 1 method to choose different multiple fileds 
    #here are the second method  
    job_city = forms.MultipleChoiceField(choices = JOB_CITY_CHOICE,
                                         widget=forms.CheckboxSelectMultiple,
                                         label='prefered Job Cities',
                                         help_text='Select 1 or more cities where you prefered to work',
                                         required=True) 

    class Meta:
        model = Profile
        fields = [
            'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file'
        ]
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'pin': 'Pin Code',
            'mobile': 'Mobile Number'
        }
        help_texts = {
                'profile_image': 'Upload a profile image (required)',
            'my_file': 'Attach a document (required)'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','id':'datepicker','type':'date'}),
            'locality': forms.TextInput(attrs={'class':'form-control','placeholder':'Write your area name'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City name'}),
            'pin': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter 6-digit PIN'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'11-digit Mobile Number'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'xyz@example.com'}),
            
            
            
        }
        



