from django.db import models
from django.core.exceptions import ValidationError   # Used for custom field validation
from django.core.validators import RegexValidator    # Used for validating mobile number format


# -----------------------------
# Custom Validator Functions
# -----------------------------
def validate_pin_address(value):
    """
    Custom validator for 'pin' field.
    Ensures that the PIN code must be exactly 6 digits long.
    """
    if len(str(value)) != 6:
        raise ValidationError('The PIN code must be exactly 6 digits.')


# -----------------------------
# Example Hardcoded Choices (Indian States)
# Later you can replace with Pakistani Provinces or load dynamically from API/DB.
# -----------------------------
STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)


# -----------------------------
# Profile Model
# -----------------------------
class Profile(models.Model):
    """
    Profile model to store user details.
    Includes validation for PIN code, mobile number, and email.
    """

    # Basic Information
    name = models.CharField(max_length=100)               # Full name of the person
    dob = models.DateField()                              # Date of birth
    gender = models.CharField(max_length=1)               # Gender (M/F/Other)

    # Address Information
    locality = models.CharField(max_length=100)           # Local area or street name
    city = models.CharField(max_length=100)               # City name
    pin = models.PositiveIntegerField(                    # PIN code (exactly 6 digits)
        validators=[validate_pin_address],
        help_text='Enter a 6-digit PIN code'
    )
    state = models.CharField(                             # State field (dropdown choices)
        choices=STATE_CHOICES,
        max_length=100
    )

    # Contact Information
    mobile = models.CharField(                            # Mobile number (must be 11 digits)
        max_length=11,
        validators=[RegexValidator(regex=r'^\d{11}$', message="Mobile number must be 11 digits")],
        help_text='Enter an 11-digit mobile number'
    )
    email = models.EmailField()                           # Email address (with proper validation)

    # Job / Other Info
    job_city = models.CharField(max_length=50)            # Preferred job location

    # Media Fields
    profile_image = models.ImageField(                    # Profile photo (optional)
        upload_to='profileimg',
        blank=True,
        null=True
    )
    my_file = models.FileField(                           # File upload (optional)
        upload_to='doc',
        blank=True,
        null=True
    )

    def __str__(self):
        """String representation of the model"""
        return self.name
