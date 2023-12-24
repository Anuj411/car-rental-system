from django.urls import path
from app_modules.seller import views

app_name = "seller"

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("car-list/", views.CarListDataTableView.as_view(), name="car_list"),
    path("update-profile/<int:pk>", views.UpdateProfileView.as_view(), name="update_profile"),
    path("profile-image/", views.GetProfileImageView.as_view(), name="get_profile_image"),
]
