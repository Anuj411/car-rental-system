from django.contrib import admin
from django.urls import path, include
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
    path('', include('users.urls')),
    path('', include('customer.urls')),
    path('', include('home.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('', include(urls.urlpatterns)),
]