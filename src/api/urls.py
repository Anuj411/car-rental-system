from django.urls import path, include

urlpatterns = [
    path('users/', include('users.api.urls')),
    path('car/', include('car.api.urls')),
]