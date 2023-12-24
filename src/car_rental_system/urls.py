from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('select2/', include('django_select2.urls')),
    path('', include('users.urls')),
    path('', include('customer.urls')),
    path('', include('seller.urls')),
    path('car/', include('car.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(urls.urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)