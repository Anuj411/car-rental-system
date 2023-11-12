from rest_framework import routers
from app_modules.users.api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'user', views.LoginView, basename="login")

urlpatterns = router.urls