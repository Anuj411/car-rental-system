from rest_framework import routers
from app_modules.users.api import views
from django.urls import path, include

app_name = "users_api"

router = routers.SimpleRouter()
router.register(r'user', views.LoginView, basename="login")
router.register(r'user', views.UserCreateApiView)

urlpatterns = router.urls

# urlpatterns = [
#     path("login/", views.LoginView.as_view(actions={'post':'login'}), name="login"),
#     path("create/", views.UserCreateApiView.as_view, name="user_create"),
# ]