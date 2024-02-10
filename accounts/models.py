from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Users must have a phone number")

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user


# create super user 
    def create_superuser(self, phone_number, password=None):
        user = self.create_user(phone_number = phone_number)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


#   Create Staff User
    def create_staffuser(self, phone_number, password=None):
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    AccountType = (
        ('individual', 'Individual'),
        ('organization', 'Organization')
    )
    username = models.CharField(max_length=255, unique=True)
    account_type = models.CharField(max_length=20, choices=AccountType, default="individual")
    phone_number = models.IntegerField(max_length=15, unique=True)
    account_created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def has_module_perms(self, app_label):
        return self.is_active
    def has_perm(self, perm, obj=None):
        return True
    def __str__(self):
        return self.username

GenderType = models.Choices("GenderType", "Male Female Other")
IDCardType = models.Choices("IDCard", "NID Passport Driving")
BloodGroup = models.Choices("BloodGroup", "A+ A- B+ B- AB+ AB- O+ O-")


class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    id_card_type = models.CharField(max_length=20, choices=IDCardType)
    id_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField()
    present_address = models.TextField()
    permanent_address = models.TextField()
    gender = models.CharField(max_length=10, choices=GenderType)
    profession = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=5, choices=BloodGroup)
    current_location = models.CharField(max_length=255)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_verified + " " + self.blood_group

