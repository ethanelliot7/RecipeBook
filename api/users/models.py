from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Profile(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)  # Make email required and unique
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profile_picture/")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']