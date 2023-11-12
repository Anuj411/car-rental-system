from rest_framework.viewsets import ViewSet

from rest_framework.response import Response
from rest_framework import status

from allauth.account import app_settings
from allauth.account.forms import LoginForm
from django.apps import AppConfig
from rest_framework.decorators import action

from app_modules.users.api.serializers import LoginSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

class LoginView(ViewSet):
    queryset = User.objects.all()

    @action(methods=["post"], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.filter(email = email).last()
            if not user:
                return Response({"error": "Email doesn't exist !!!"})
            
            if(user.check_password(password)):
                return Response({"success": "Login successfully !!!"})
            else:
                return Response({"error": "Password is incorrect !!!"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)