from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from accounts.apis.serializers.account_serializer import AccountSerializer

from accounts.models import Account


class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
