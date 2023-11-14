from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("user_permissions")
        data.pop("groups")
        return data