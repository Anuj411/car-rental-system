from django.urls import path
from app_modules.users import views

app_name = "users"

urlpatterns = [
    path('login', views.LoginRegistrationView.as_view(), name="register_login"),
    path('auth/login', views.LoginView.as_view(), name="login"),
]
