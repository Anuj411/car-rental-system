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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["autofocus"] = False
