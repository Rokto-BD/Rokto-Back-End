from django.urls import path

from accounts.apis.views.account_api import AccountCreateAPIView


urlpatterns = [
    path("signup/", AccountCreateAPIView.as_view(), name="account_create"),
]
