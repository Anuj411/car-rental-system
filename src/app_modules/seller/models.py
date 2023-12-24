from django.db import models
from app_modules.base.models import BaseModel

from django.contrib.auth import get_user_model
User = get_user_model()


class Seller(BaseModel):
    gst_no = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller_set")