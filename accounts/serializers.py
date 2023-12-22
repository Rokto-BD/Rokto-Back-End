
from rest_framework import serializers

from accounts.models import Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'account_type', 'is_verified', 'account_created_at' ]

