from django import forms
from account.models import User


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "name", "password", "confirm_password"]

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            confirm_password = cleaned_data.get('confirm_password')

            if password != confirm_password:
                self.add_error('confirm_password',
                               'Password and Confirm Password do not match.')

            return cleaned_data

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "A user with this email already exists.")
            return email
        
        
        
class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if a user with this email exists
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                ('No account is associated with this email address.')
            )
        return email