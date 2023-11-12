from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseUser(AbstractUser):
    profile_image = models.ImageField(upload_to="user/profile", null=True, blank=True)