from django.urls import path
from app_modules.home import views

app_name = "home"

urlpatterns = [
    path('address/', views.addressCreateView.as_view(), name="address"),
]
