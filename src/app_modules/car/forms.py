from django import forms
from app_modules.car.models import Car, CarImage


class CarCreateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = "__all__"


class CarImageCreateForm(forms.ModelForm):

    class Meta:
        model = CarImage
        fields = ["order", "title", "image", "car"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_order(self):
        order = self.cleaned_data["order"]

        if order == 0:
            raise forms.ValidationError("Order cannot zero.")
        return order
