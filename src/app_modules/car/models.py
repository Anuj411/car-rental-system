from email.policy import default
from django.db import models
from app_modules.base.models import BaseModel


class Car(BaseModel):
    _4_SEATER = "4 Seater"
    _6_SEATER = "6 Seater"
    _7_SEATER = "7 Seater"

    CAR_TYPES = (
        ("4 Seater", _4_SEATER),
        ("6 Seater", _6_SEATER),
        ("7 Seater", _7_SEATER),
    )

    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=CAR_TYPES)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey("users.BaseUser", on_delete=models.CASCADE, related_name="car_set", null=True, default=None)

    def get_image(self):
        return self.image_set.first().image.url or "" # type: ignore

    def __str__(self):
        return self.model


class CarImage(BaseModel):
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car")
    title = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="image_set")