from django import forms 
from todo.models import TODOO
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError   

def validate_pin_address(value):
    if len(str(value)) < 8:
        raise ValidationError('Password must be 8 digits')


class Customsigninform(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'inp', 'placeholder': '********'}
        ),
        label='Password',
        validators=[validate_pin_address],
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': "FULL Name",
            'email': "Email",
            'password': "Password"
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'inp', 'placeholder': 'Enter Name'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'inp', 'placeholder': 'xyz@example.com'}
            ),  
        }
        error_messages = {
            'username': {
                'required': " Username is required.",
              
            },
            'email': {
                'required': " Email is required.",
                'invalid': " Enter a valid email address.",
            },
            'password': {
                'required': " Password is required.",
            }
        }

        help_texts = {
            'username': None,
            'email': None,
            'password': None,
        }
