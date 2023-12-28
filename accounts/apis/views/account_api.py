from accounts.apis.serializers.account_serializer import AccountSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.models import Account


class AccountCreateAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
