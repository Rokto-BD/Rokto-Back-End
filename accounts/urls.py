from django.urls import path,include
from accounts.apis.urls.account_url import urlpatterns as account_urls


urlpatterns = [
    path('', include(account_urls)),
]
