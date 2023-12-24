from api.viewsets import BaseModelViewSet, BaseViewSet
from rest_framework.response import Response
from rest_framework import status

from allauth.account import app_settings
from django.apps import AppConfig
from rest_framework.decorators import action

from app_modules.car.api.serializers import CarCreateSerializer
from app_modules.car.models import Car

# from django.contrib.auth import get_user_model
# User = get_user_model()

class CarCreateApiView(BaseModelViewSet):
    serializer_class = CarCreateSerializer
    queryset = Car.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.save()
        
        return Response(
            {"success": "Car created."},
            status=status.HTTP_200_OK
        )
    
    