from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Profile(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to="api/users/profilepicture")