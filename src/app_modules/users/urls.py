from django.urls import path
from app_modules.users import views

app_name = "users"

urlpatterns = [
    path('login/', views.LoginSignupView.as_view(), name="login_signup"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('seller/signup/', views.SellerSignupView.as_view(), name="seller_signup"),
    path('auth/login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
