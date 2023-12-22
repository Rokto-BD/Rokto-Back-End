from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['user', 'phone_number', 'account_type', 'is_verified']
