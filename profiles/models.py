from django.db import models
from django.conf import settings


class Gender(models.TextChoices):
    
    MALE = "Male" , "Male"
    FEMALE = "Female", "Female"
    OTHER = "Other", "Other"

class Profile(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank = True,
        null = True
    )
    
    bio = models.TextField(
        max_length = 150,
        blank = True
    )
    
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    
    gender = models.CharField(
        max_length=10,
        choices = Gender.choices
    )
    
    mobile_number = models.CharField(
        max_length=15,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
