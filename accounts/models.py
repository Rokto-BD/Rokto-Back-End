from django.contrib.auth.models import User
from django.db import models

# Create your models here.


AccountType = models.TextChoices("Individual", "Organization")


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    account_type = models.CharField(max_length=3, choices=AccountType)
    is_verified = models.BooleanField(default=False)



GenderType = models.TextChoices("Male", "Female", "Other") )

class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    id_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField()
    present_address = models.TextField()
    permanent_address = models.TextField()
    gender = models.CharField(max_length=1, choices=GenderType)
    profession = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5)
    current_location = models.CharField(max_length=255)
