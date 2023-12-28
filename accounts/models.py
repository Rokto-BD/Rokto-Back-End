from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("Users must have a phone number")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number=phone_number, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    AccountType = (
        ('individual', 'Individual'),
        ('organization', 'Organization')
    )

    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=20, choices=AccountType, default="individual")
    phone_number = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    account_created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'username', 'email', 'account_type']

    objects = UserManager()


    def has_module_perms(self, app_label):
        return self.is_active


GenderType = models.Choices("GenderType", "Male Female Other")
IDCardType = models.Choices("IDCard", "NID Passport Driving")
BloodGroup = models.Choices("BloodGroup","A+ A- B+ B- AB+ AB- O+ O-")


class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
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
