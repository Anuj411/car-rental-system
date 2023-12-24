from api.serializers import BaseModelSerializer
from app_modules.car.models import Car, CarImage
from rest_framework import serializers

class CarImageSerializer(BaseModelSerializer):
    class Meta:
        model = CarImage
        fields = ("image",)

class CarCreateSerializer(BaseModelSerializer):
    image_set = serializers.ListField(child=serializers.CharField(max_length=254))

    class Meta:
        model = Car
        fields = ("model_name", "type", "company", "seller", "image_set")
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data.pop("user_permissions")
    #     data.pop("groups")
    #     return data