from django.contrib import admin
from accounts.models import Profile, Account

# Register your models here.

admin.site.register(Account)
admin.site.register(Profile)