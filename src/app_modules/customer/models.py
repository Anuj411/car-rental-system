from django.db import models
from app_modules.base.models import BaseModel

from django.contrib.auth import get_user_model
User = get_user_model()

class Customer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_set")

class State(BaseModel):
    name = models.CharField(max_length=100)
    car = models.ForeignKey("car.Car", on_delete=models.CASCADE, related_name="state_set", null=True, default=None)
    