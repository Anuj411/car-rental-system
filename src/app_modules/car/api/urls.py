from rest_framework import routers
from app_modules.car.api import views
from django.urls import path, include

app_name = "car_api"

router = routers.DefaultRouter()
router.register(r'', views.CarCreateApiView)

urlpatterns = router.urls
