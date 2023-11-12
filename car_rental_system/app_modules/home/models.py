from django.db import models
from app_modules.base.models import BaseModel

class Country(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(BaseModel):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="state_set")

    def __str__(self):
        return self.name

class City(BaseModel):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(State, on_delete=models.CASCADE, related_name="city_set")

    def __str__(self):
        return self.name