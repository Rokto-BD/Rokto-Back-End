from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('accounts.urls')),
    # path('', include(router.urls)),
]
