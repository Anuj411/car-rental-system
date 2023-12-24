from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2",
            )


class SellerForm(UserForm):
    gst_no = forms.CharField(max_length=15)
    
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "gst_no",
        )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field.widget.is_hidden is False:
                field.required = True
    