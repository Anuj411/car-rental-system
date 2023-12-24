from django.urls import path
from app_modules.customer import views

app_name = "customer"

urlpatterns = [
    path('', views.homeView.as_view(), name="home"),
]
