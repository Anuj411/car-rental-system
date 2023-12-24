from django.db import models
from django.contrib.auth.models import AbstractUser


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

    @property
    def get_profile_image(self):
        return self.profile_image.url if self.profile_image else ""