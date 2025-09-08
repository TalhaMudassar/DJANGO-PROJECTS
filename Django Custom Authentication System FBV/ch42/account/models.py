from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManger(BaseUserManager):
    """
    Custom manager to create users with email as the unique identifier.
    """

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("User must have a valid email address")
        # normalize_email lowercases the domain part
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)  # hashes the raw password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a Superuser with the given email and password.
        We force is_staff and is_superuser True for admin access.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser=True.')

        user = self.create_user(email, password)
        # Optional project-specific roles
        user.is_staff = True
        user.is_superuser = True
        user.is_customer = True
        user.is_seller = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    Minimal custom user model using email instead of username.
    AbstractBaseUser provides: password, last_login, is_active (we override), etc.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)              # make blank=True if optional
    city = models.CharField(max_length=255)              # make blank=True if optional

    # Activation/roles
    is_active = models.BooleanField(default=False)       # must manually activate or via link
    is_staff = models.BooleanField(default=False)        # admin site access
    is_superuser = models.BooleanField(default=False)    # full permissions
    is_customer = models.BooleanField(default=True)      # role flag
    is_seller = models.BooleanField(default=False)       # role flag

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True) # when created
    updated_at = models.DateTimeField(auto_now=True)     # last updated

    # Use email for authentication instead of username
    USERNAME_FIELD = 'email'

    # Attach custom manager
    objects = UserManger()

    def __str__(self):
        return self.email

    # Permissions: keep it simple for this project (superuser = all perms)
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
