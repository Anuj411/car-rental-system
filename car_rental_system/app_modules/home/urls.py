from django.urls import path
from app_modules.home import views

app_name = "home"

urlpatterns = [
    path('', views.homeView.as_view(), name="home"),
    path('address/', views.addressCreateView.as_view(), name="home"),
]
