from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseUser(AbstractUser):
    CUSTOMER = "Customer"
    SELLER = "Seller"

    ROLE_CHOICES = (
        (CUSTOMER, CUSTOMER),
        (SELLER, SELLER),
    )

    email = models.EmailField(("email address"), unique=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default=CUSTOMER)
    profile_image = models.ImageField(upload_to="user/profile", null=True, blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []