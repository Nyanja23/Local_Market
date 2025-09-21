from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ('vendor','Vendor'),
    ('customer','Customer'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

