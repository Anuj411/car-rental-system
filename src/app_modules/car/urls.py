from django.urls import path
from app_modules.car import views

app_name = "car"

urlpatterns = [
    path("", views.CarListView.as_view(), name="list_car"),
    path("create", views.CarCreateView.as_view(), name="create_car"),
    path("<int:pk>/update", views.CarUpdateView.as_view(), name="update_car"),
]
